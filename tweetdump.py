from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json


# Start a listener
class StdOutListener(StreamListener):

    def on_data(self, data):
	tweet = json.loads(data)
	#Twitter sends the userstream account friends. Anyway, we'll EAFP that
	try:
		print tweet["created_at"] + ","+ tweet["user"]["screen_name"] + "," + tweet["text"]
        except:
		pass # So pro. I should probably handle the exception, but no. No I won't.
	return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    #Grab API creds from config.py
    config = {}
    execfile("config.py", config)

    #Auth to Twitter
    listener = StdOutListener()
    auth = OAuthHandler(config["consumer_key"],config["consumer_secret"])
    auth.set_access_token(config["access_token"], config["access_token_secret"])
    stream = Stream(auth, listener)

    stream.userstream(_with='followings')
