from tweepy import API
#extract tweets from cursor from your own timeline or friend's timeline
from tweepy import Cursor
#firehose of tweets
from tweepy.streaming import StreamListener
#for authenticating based on credentials
from tweepy import OAuthHandler
from tweepy import Stream
#data processing 
import numpy as np 
import pandas as pd 

'''TWITTER CLIENT'''
class TwitterClient():
    def __init__(self,twitteruser=None):
        #authenticator
        self.auth=TwitterAuthenticator().authenticatetwitterapp()
        self.twitterclient=API(self.auth)

    #PROCESSING
    #create function to get twitterclient api to interface with api and extract data from tweets we get
    def gettwitterclientapi(self):
        return self.twitterclient 
        #get information from a specific user other than you
        self.twitteruser=twitteruser

    #function to get tweets
    #num tweets is how many tweets we want to extract
    def get_usertimelinetweets(self,num_tweets):
        tweets=[]
        #loop through certain number of tweets for each tweet we store in list and return list to user
        #import a cursor to get user timeline tweets
        #from API class there is a method: .user_timeline
        #parameter for cursor object .items() will tell how many tweets to get from timeline 

        for tweet in Cursor(self.twitterclient.user_timeline, id=self.twitteruser).items(num_tweets):
            tweets.append(tweet)
        #returning tweets list of timeline tweets 
        return tweets 
    def getfriendlist(self,num_friends):
        friendlist=[]
        for friend in Cursor(self.twitterclient.friends, id=self.twitteruser).items(num_friends):
            friendlist.append(friend)
        return friendlist
    def gethometimelinetweets(self,num_tweets):
        hometimelinetweets=[]
        for tweet in Cursor(self.twitterclient.home_timeline, id=self.twitteruser).items(num_tweets):
            hometimelinetweets.append(tweet)
        return hometimelinetweets


'''TWITTER AUTHENTICATOR'''
class TwitterAuthenticator():
    def authenticatetwitterapp(self):
        #want to authenticate
#oauthhandler is class we import from tweepy responsible for authenticating
        auth=OAuthHandler("vFutoJoPIDaF8O3U3ifJUnrFw",
        "Gfy8ykTjnHf7gxj0kkakRWqY9gWhDEd69aHDWewAWP2hsxCv0z")
#in order to define auth object of the oauthhandler class it takes those
#two arguments^^
#to complete authentication process a method provided from oauthhandler class
        auth.set_access_token("855588527039422465-BirmEI78Vvugvm44y5cJzNoMjPiF8B8",
        "RjZhI9lCoptKipRcKnPV6Uu4mIa4L0CGk9FoBXJ7GJNnB")
        return auth 


'''TWITTER STREAMER - CLASS FOR STREAMING AND PROCESSING LIVE TWEETS'''
class TwitterStreamer():

    def __init__(self):
        #authentication occurs in constructor
        self.twitterauthenticator=TwitterAuthenticator()

    #want to be able to save tweets to txt or json
    #pass in a filename where we want to write our tweets to
    #hash_tag_list=filter for hashtags and keywords
    def stream_tweets(self, fetched_tweet_filename, hash_tag_list):

#create listener object
#StdOutListener is a class that handles tweets recieved from a stream 
        listener=TwitterListener(fetched_tweet_filename)
        #defining auth for the stream below. using class TwitterAuthenticator() and method authenticatetwitterapp()
        auth=self.twitterauthenticator.authenticatetwitterapp()

#create a twitter stream. pass authentication token and listener objectself
#listener prints data and errors
        stream=Stream(auth,listener)
#filter. Want to stream tweets focused on filters and hashtags
#filter takes a list called track list.
        stream.filter(track=hash_tag_list)

#object oriented lucidprogramming. create class to print tweets
#class will inherit from stream listener class
#stream listener class which we can override

'''TWITTER STREAM LISTENER - A BASIC LISTENER THAT PRINTS RECIEVED TWEETS TO STDOUT'''
class TwitterListener(StreamListener):
#methods we will be overriding: on_data and on_error
#take in data for streamed listener and print
    #create a constructor for where we want to store the tweets
    def __init__(self,fetched_tweet_filename):
        self.fetched_tweet_filename = fetched_tweet_filename

    def on_data(self, data):
        #make better for errors
        try:
            print(data)
            #want to write to a file. will append because we want to
            #keep write tweets to it as we stream
            with open(self.fetched_tweet_filename,'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            #if that exception is hit, then we print out actual error message
            print("Error on data: %s" % str(e))
        return True

    #if there is an error that occurs print status message of error 
    def on_error(self, status):
        #420 message means you are exceeding rate limit. need to wait to access tweets again
        if status==420:
            return False
        print(status)
#DATA PROCESSING - CLASS FOR ANALYZING AND CATEGORIZING CONTENT FROM TWEETS 
class TweetAnalyzer():
    #create a dataframe to store tweets from Donald Trump
    def tweets_to_dataframe(self,tweets):
        #create dataframe object with pandas DataFrame function
        #specificy data. give data a list. list will be created from tweets from this function
        #extracting text from tweet 
        #DATA VARIABLE GOING INTO DATAFRAME FUNCTION. CREATING A LIST AND LOOPING FOR EVERY TWEET IN TWEETS. 
        #EXTRACTING TEXT FROM EACH OF THOSE TWEETS
            #THEN SPECIFYING THE COLUMN WHERE THIS WILL LIVE IN DATAFRAME. GIVING COLUMN AS NAME 'TWEETS'
        df=pd.DataFrame(data=[tweet.text for tweet in tweets],columns=['TWEETS'])
        return df







#create an object from this stdoutlistner class
#This conditional is used to check whether a python module is being run directly or being imported.
if __name__=="__main__":
    #DATA PROCESSING-GET API to get the tweets before we analyze
    #CREATE A TWEET ANALYZER OBJECT FOR CLASS WE CREATED ABOVE
    tweet_analyzer=TweetAnalyzer()
    twitter_client=TwitterClient()
    api=twitter_client.gettwitterclientapi()
    #WANT TO STREAM TWEETS FROM TIMELINE FOR DATA PROCESSING - function from twitter api -screename, count
    tweets=api.user_timeline(screen_name="realDonaldTrump",count=20)

    df=tweet_analyzer.tweets_to_dataframe(tweets)
    #print first 10 elements
    print(df.head(10))
    
    
    #hash_tag_list=["donald trump","hillary clinton"]
    #fetched_tweet_filename="tweets.json"
    #define a twitter streamer object
    #twitter_streamer=TwitterStreamer()
    #twitter_streamer.stream_tweets(fetched_tweet_filename,hash_tag_list)
#######gettting timeline tweets######
    #twitter_client=TwitterClient('pycon')
    #print(twitter_client.get_usertimelinetweets(5))
