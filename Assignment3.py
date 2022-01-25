# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 08:24:57 2021

@author: FaSa79_
"""

import tweepy
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'S8QvO5JPH1IV01LVDZuBq65w2'
consumer_secret = 'B9J9pguDm6a5Ey97iPi3FPZG8U6BuhzElNDs9vHGCTb9GXMjHS'
access_token = '1248812219405488128-SvSL0UYJ3OAsSyKfo8Vx6kuDhoxypH'
access_secret = 'pvZOuusaiazpUjLpojsvq43gCFFxd5bfSqigg0AxnymTW'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API (auth)
file = open('Covid19_Vaccines_raw.dat','a')

class MyListener(StreamListener):
    
    def __init__(self, api = None):
        super(StreamListener, self).__init__()
        self.num_tweets = 0
        
    def on_data(self, data):
        
        try:
            with open('Covid19_Vaccines.dat','a') as f:
                tweet = json.loads(data)
                
                if (tweet['lang']) == "en":
                    #file.write(data)
                    #file.write('\n')
                    #print(tweet['text'])
                    
                    if self.num_tweets < 50:
                        #print(json.dumps(tweet['text'], indent = 4))
                        file.write(data)
                        file.write('\n')
                        f.write(tweet['extended_tweet']['full_text'])
                        print(tweet['extended_tweet']['full_text'])
                        f.write("\n")
                        self.num_tweets = self.num_tweets + 1
                        print(self.num_tweets)
                        return True    
            
                return True
            
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        
        return True
    
    def on_error(self, status):
       print(status)
       return True
   
    def on_status(self, status):
        if status.retweeted_status == 'true' :
            return 
        print(status)

def listeningTweet():
    tweet_listener = MyListener()
    mytwitter_stream = Stream(auth, tweet_listener)
    
    mytwitter_stream.filter(track = ['#Pfizer','#PFizer','#PFIZER','#pfizer','#pFizer','Pfizer','PFizer','PFIZER','pfizer','pFizer'])

    
file.close()
print("Done")