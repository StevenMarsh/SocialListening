import sys
from sentdex.streamtweetssentiment import streamTweets
from newstuff.IBMWatson import ibmtoneanalyzer

def userInputHandler():
    keyword = sys.argv[1]
    location = sys.argv[2]
    time = int(sys.argv[3])

    # if twitter, start streaming twitterStream(keyword, location, time)
    streamTweets(keyword,location,time)
    twitter=True
    # if reddit, start streaming
    reddit=False
    # parse through custom text file
    custom=""#TODO change
    # call ibmtoneanalyzer(twitter=twitter, reddit=reddit, custom=custom
    ibmtoneanalyzer.IBMToneAnalysis(twitter,reddit,custom)
    # write output

    print(keyword, location, time)


userInputHandler()