from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#json library to load data
import json
#CONNECTING SQLITE DATABASE
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import time
import re

conn = sqlite3.connect('twitter.db')
c = conn.cursor()
#CREATING SQLITE TABLE
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")
    conn.commit()

create_table()
#SENTIMENT ANALYSIS ANALYZER
analyzer = SentimentIntensityAnalyzer()

# consumer key, consumer secret, access token, access secret.
auth = OAuthHandler("vFutoJoPIDaF8O3U3ifJUnrFw",
        "Gfy8ykTjnHf7gxj0kkakRWqY9gWhDEd69aHDWewAWP2hsxCv0z")
auth.set_access_token("855588527039422465-BirmEI78Vvugvm44y5cJzNoMjPiF8B8",
        "RjZhI9lCoptKipRcKnPV6Uu4mIa4L0CGk9FoBXJ7GJNnB")

class listener(StreamListener):

    def __init__(self):
        self.__endTime = time.time() + 20

    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = data["extended_tweet"]["full_text"]

            url = re.search("https://t.co/\w\w\w\w\w\w\w\w\w\w", tweet)
            if url:
                tweet = re.sub(url.group(), " ", tweet)

            time_ms = data['timestamp_ms']
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            print(time_ms, tweet, sentiment)
            c.execute("INSERT INTO sentiment (unix, tweet, sentiment) VALUES (?, ?, ?)",
                  (time_ms, tweet, sentiment))
            conn.commit()

            if time.time() > self.__endTime:
                return False
        except KeyError as e:
            nothing = e
        return True


    def on_error(self, status):
        print(status)


def main():
    try:
        twitterStream = Stream(auth, listener())


        twitterStream.filter(track=["@realDonaldTrump"], languages=["en"])

        time.sleep(runtime)

        twitterStream.filter(track=["@realDonaldTrump"], languages=["en"])

        twitterStream.disconnect()
    except Exception as e:
        print(str(e))
        time.sleep(5)


main()