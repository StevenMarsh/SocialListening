import tweepy
import datetime
import sys
from datetime import datetime, date,timedelta





def my_function(query, num):
    # credentials from https://apps.twitter.com/
    consumerKey = "vFutoJoPIDaF8O3U3ifJUnrFw"
    consumerSecret = "Gfy8ykTjnHf7gxj0kkakRWqY9gWhDEd69aHDWewAWP2hsxCv0z"
    accessToken = "855588527039422465-BirmEI78Vvugvm44y5cJzNoMjPiF8B8"
    accessTokenSecret = "RjZhI9lCoptKipRcKnPV6Uu4mIa4L0CGk9FoBXJ7GJNnB"

    N = 1
    date_today = datetime.now();
    date_N_days_ago = datetime.now() - timedelta(days=N)

    x = str(date_N_days_ago.strftime("%Y-%m-%d"))
    y = str(date_today.strftime("%Y-%m-%d"))
   # print (x + " "+  y)

    # until	optional	Returns tweets created before the given date. Date should be formatted as YYYY-MM-DD. Keep in mind that the search index has a 7-day limit. In other words, no tweets will be found for a date older than one week.

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    api = tweepy.API(auth)
    searched_tweets = api.search(q=query, count=num, since=x, until=y)

    for result in searched_tweets:
        print(result.text)

def main():
    my_function(query = "hello", num = 100);

main()

# username = "@twitter"
# startDate = datetime.datetime(2019, 9, 1, 0, 0, 0)
# endDate =   datetime.datetime(2019, 10, 1, 0, 0, 0)
#
# tweets = []
# tmpTweets = api.user_timeline(username)
# for tweet in tmpTweets:
#     if tweet.created_at < endDate and tweet.created_at > startDate:
#         tweets.append(tweet)
#
# while (tmpTweets[-1].created_at > startDate):
#     tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
#     for tweet in tmpTweets:
#         if tweet.created_at < endDate and tweet.created_at > startDate:
#             tweets.append(tweet)
#
# for tweet in tweets:
#     print(tweet)