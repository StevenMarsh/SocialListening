from tweepy import Stream
from tweepy import OAuthHandler
import tweepy
import sys
from tweepy.streaming import StreamListener


auth = OAuthHandler("vFutoJoPIDaF8O3U3ifJUnrFw",
        "Gfy8ykTjnHf7gxj0kkakRWqY9gWhDEd69aHDWewAWP2hsxCv0z")
auth.set_access_token("855588527039422465-BirmEI78Vvugvm44y5cJzNoMjPiF8B8",
        "RjZhI9lCoptKipRcKnPV6Uu4mIa4L0CGk9FoBXJ7GJNnB")
api = tweepy.API(auth,  wait_on_rate_limit=True)


replies = []
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

for full_tweets in tweepy.Cursor(api.user_timeline,screen_name='arresteddev',timeout=999999).items(10):
  for tweet in tweepy.Cursor(api.search,q='to:arresteddev', since_id=1106525453018230784, result_type='recent',timeout=999999).items(1000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
      if (tweet.in_reply_to_status_id_str==full_tweets.id_str):
        replies.append(tweet.text)
  print("Tweet :",full_tweets.text.translate(non_bmp_map))
  for elements in replies:
       print("Replies :",elements)
  replies.clear()


# def main():
#   try:
#       twitterStream = Stream(auth, listener())
#       twitterStream.filter(track=["cwe"], languages=["en"])
#       time.sleep(runtime)
#       twitterStream.disconnect()
#   except Exception as e:
#       print(str(e))
#       time.sleep(5)
#
#
# main()