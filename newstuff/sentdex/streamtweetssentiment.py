from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import gmaps
import gmaps.datasets

import googlemaps
from datetime import datetime

#json library to load data
import json
#CONNECTING SQLITE DATABASE
import sqlite3

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


# consumer key, consumer secret, access token, access secret.
auth = OAuthHandler("vFutoJoPIDaF8O3U3ifJUnrFw",
        "Gfy8ykTjnHf7gxj0kkakRWqY9gWhDEd69aHDWewAWP2hsxCv0z")
auth.set_access_token("855588527039422465-BirmEI78Vvugvm44y5cJzNoMjPiF8B8",
        "RjZhI9lCoptKipRcKnPV6Uu4mIa4L0CGk9FoBXJ7GJNnB")

class listener(StreamListener):


    def __init__(self):
        self.__endTime = time.time() + 20 #20 represents time that class will be streaming tweets into DB (live feed)

    def on_data(self, data): #always include self on class methods
        try:
            data = json.loads(data)
            tweet = data["extended_tweet"]["full_text"] #grab tweets in JSON format

            url = re.search("https://t.co/\w\w\w\w\w\w\w\w\w\w", tweet) #TODO removes URLs from Tweets
            if url:
                tweet = re.sub(url.group(), " ", tweet) #remove url from tweet-- not working

            time_ms = data['timestamp_ms']

            c.execute("INSERT INTO sentiment (unix, tweet) VALUES (?, ?)",
                  (time_ms, tweet))
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


        twitterStream.filter(track=["@realDonaldTrump"], languages=["en"]) #stream.filter function calls listener.on_data()
        #twitterStream.filter(locations=["LA"]) #TODO figure out what this does and how to use
        #GoogleMaps API to extract long and lat from location ??? look into TODO
        #gmaps = googlemaps.Client(key='Add Your Key here')
        gmaps.configure(api_key='AIzaSyBkLGEGM59jEMlOhJGZcr4ZJLjhKHuKSs0')
        marker_location = (34.0522, 118.2437)
        fig = gmaps.figure()
        marker = gmaps.marker_layer(marker_location)
        fig.add_layer(marker)
        #
        # time.sleep(runtime)
        #
        # twitterStream.filter(track=["@realDonaldTrump"], languages=["en"])

        twitterStream.disconnect()
    except Exception as e:
        print(str(e))
        time.sleep(5)


main()