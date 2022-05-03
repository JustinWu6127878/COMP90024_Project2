import tweepy as tw
import json
import couchdb
from textblob import TextBlob
import re
import time
import sys

# 改一下自己的
consumer_key = 'KE67SJbQMuD1b0Ytl6YwXRNQl'
consumer_secret = 'A5orkbgnSeROt3iou1j2gbGNXBrSqw5RSOzNUkPXPco1Z3KjYY'
access_token = '760152742140579841-i2QA4e2eYp38cSJqNAY956YRm6QaWz8'
access_secret = '5QJq3y9lVyTsPVGgK94I4kS2yOdtOf0en34r48Y3rvmi7'

db_address = 'http://admin:123456@172.26.134.164:5984/'
try:
    couchServer =  couchdb.Server(db_address)
except Exception as e:
    print(e) 

# 也改一下自己的
# Change to your database, if the dabase exist


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
            db.save(item)

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
    melb_pos = [144.698181, -38.500893, 145.258484, -37.627284]
    syd_pos = [150.520929, -34.118347, 151.343021, -33.578141]
    perth_pos = [115.617614, -32.675715, 116.239023, -31.624486]
    bris_pos = [152.668523, -27.767441, 153.31787, -26.996845]
    adel_pos = [138.44213, -35.34897, 138.78019, -34.652564]
    
    if sys.argv[1] == 'melb':
        pos = melb_pos
    elif sys.argv[1] == 'syd':
        pos = syd_pos
    elif sys.argv[1] == 'perth':
        pos = perth_pos
    elif sys.argv[1] == 'bris':
        pos = bris_pos
    elif sys.argv[1] == 'adel':
        pos = adel_pos
    else:
        print('wrong argv')
        exit(1)

    try:
        db_key = 'vacc_' + sys.argv[1]
        db = couchServer[db_key]
    except Exception as e:
        print(e)

    myStream.filter(track=['vaccination', 'pfizer','moderna','AstraZeneca'], locations=pos,languages=['en'])


        







