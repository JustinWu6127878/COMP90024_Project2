import tweepy as tw
import json
import couchdb
from textblob import TextBlob
import re
import time

# 改一下自己的
consumer_key = 'NdUZlILXc2tfu4L2PIMmhaETf'
consumer_secret = 'rH8RKWEpvOI2h6ojBM3VkCk0pHfFc0sB2zu2GDz3oW3uhQFgkE'
access_token = '1256582863622778880-v4eFANNXxTh9vXuHTG7r7vtueqGNSr'
access_secret = 'g1IrXJi200uX2eaZ1pVxdlgWIuiQD3EweznRCaScdeNxp'

db_address = 'http://admin:123456@172.26.129.187:5984/'
try:
    couchServer =  couchdb.Server(db_address)
except Exception as e:
    print(e) 

# 也改一下自己的
# Change to your database, if the dabase exist
try:
    db = couchServer['government_syd']
except Exception as e:
    print(e)

# if the databse does not exist, use couchServer.create()
# db

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+) | ([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):

    # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def get_full_text(tweet):
    if tweet.get('truncated'):
        raw_text = tweet.get('extended_tweet')['full_text']
    else:
        raw_text = tweet.get('text')
    
    return raw_text

class MyStream(tw.Stream):

    def on_status(self, status):
        tweet = status._json
        retweet = tweet.get('retweeted_status')
        isRetweet = False
        if retweet:
            isRetweet = True
            raw_text = get_full_text(retweet)
        else:
            raw_text = get_full_text(tweet)

        if tweet['place']:
            print(tweet['place'])     

        try:
            item = {
                'id': tweet['id'],
                'truncated:': status.truncated,
                'isRetweet': isRetweet,
                'created_at': tweet['created_at'],
                'text': raw_text,
                'processed_text': clean_tweet(raw_text),
                'coordinates': tweet['coordinates'],
                'place': tweet['place'],
                'lang': tweet['lang'],
                'sentiment': get_tweet_sentiment(raw_text)              
            }
            # print(item)
            # db.save(item)

        except Exception as e:
            print(e)
       
    def on_error(self, status_code):

        print(status_code)

        if status_code == 420:
            time.sleep(10)
        elif status_code == 429:
            time.sleep(15*60)
        else:
            time.sleep(10)


if __name__ == '__main__':
    myStream = MyStream(consumer_key, consumer_secret, access_token, access_secret)
    # auth = tw.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_secret)
    # myStream = tw.Stream(auth, myStreamListener, tweet_mode='extended')

    # 这里也改一下自己的
    # Change to your keyword
    myStream.filter(track=['scott morrison', 'scomo', 'Australian prime minister', 'Daniel Andrews', 'premier of victoria'], locations=[144.698181, -38.500893, 145.258484, -37.627284])


        







