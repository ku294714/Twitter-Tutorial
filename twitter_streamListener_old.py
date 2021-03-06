'''
Twitter Stream Listener
'''


# tweepy setup
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import io
import os
import json


# twitter OAuth
ckey = '*CONSUMER KEY*'
consumer_secret = '*CONSUMER SECRET*'
access_token_key = '*ACCESS TOKEN*'
access_token_secret = '*ACCESS SECRET*'


#Listener Class Override

class listener(StreamListener):

	def __init__(self, start_time, time_limit=60):

		self.time = start_time
		self.limit = time_limit

	def on_data(self, data):

		while (time.time() - self.time) < self.limit:

			try:

				saveFile = open('raw_tweets_old.json', 'a')
				saveFile.write(data)
				saveFile.write('\n')
				saveFile.close()

				return True


			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass

		exit()

	def on_error(self, status):

		print status

	def on_disconnect(self, notice):

			print 'bye'



#Beginning of the specific code
start_time = time.time() #grabs the system time

keyword_list = ['emoji'] #track list


auth = OAuthHandler(ckey, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)


twitterStream = Stream(auth, listener(start_time, time_limit=200)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Listener


