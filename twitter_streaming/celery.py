import json
import os

import dateutil.parser
import django
from celery import Celery
from django.utils.encoding import uri_to_iri
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

os.environ['DJANGO_SETTINGS_MODULE'] = 'twitter_streaming.settings'

# to load tweetInfo model
django.setup()
from twitter_api.models import TweetInfo

os.environ.setdefault('RQ_QUEUES', 'twitter_streaming.settings')
celery = Celery('twitter_streaming')
celery.autodiscover_tasks()

# Variables that contains the user credentials to access Twitter API
access_token = "817355436995190785-9NNNFpwhtQRxZJUAWHCXDZLzqNfQ3Dq"
access_token_secret = "JTpYExcLDllGARXsHOgJrkVvFCTJcbdEGb4acwPZq7wFt"
consumer_key = "9czzvO7F3m5eJHdJ6dMAs0ZhW"
consumer_secret = "RZicUxfALTnG4bRmSof2b0o95Xc1bijZ0fOTw8rmUAAACET2ep"


def save_tweets(data):
    # print(data)
    try:
        tweet = json.loads(data)
        if 'created_at' in tweet:
            tweetInfo = TweetInfo()
            tweetInfo.created_at = dateutil.parser.parse(tweet['created_at'])
            if len(tweet['text']) >= 500:
                tweetInfo.text = uri_to_iri(str(tweet['text'][0:500]))
            else:
                tweetInfo.text = uri_to_iri(str(tweet['text']))
            tweetInfo.user_name = uri_to_iri(str(tweet['user']['name']))
            tweetInfo.screen_name = str(tweet['user']['screen_name'])
            tweetInfo.user_favorite_count = tweet['user']['favourites_count']
            tweetInfo.user_followers_count = tweet['user']['followers_count']
            tweetInfo.user_friends_count = tweet['user']['friends_count']
            tweetInfo.quote_count = tweet['quote_count']
            tweetInfo.favorite_count = tweet['favorite_count']
            tweetInfo.retweet_count = tweet['retweet_count']
            tweetInfo.reply_count = tweet['reply_count']
            tweetInfo.language = tweet['lang']
            tweetInfo.hash_tags_count = len(tweet['entities']['hashtags'])
            hashtags = []
            try:
                for i in range(0, len(tweet['entities']['hashtags'])):
                    hashtags.append(tweet['entities']['hashtags'][i]['text'])
                tweetInfo.set_hashtags(hashtags)
            except:
                print('hash_error')

            tweetInfo.user_mentions_count = len(tweet['entities']['user_mentions'])
            user_mentions = []
            try:
                for i in range(0, len(tweet['entities']['user_mentions'])):
                    user_mentions.append(tweet['entities']['user_mentions'][i]['name'])
                tweetInfo.set_user_mentions(user_mentions)
            except:
                print('user_mentions_error')

            tweetInfo.save()
            print("added")
    except:
        print("error")


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        save_tweets(data)
        # print(data)
        return True

    def on_error(self, status):
        print(status)


@celery.task()
def startup():
    print("Started")
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)
    # stream.sample()
    while True:
        try:
            stream.sample()
        except:
            print("time out")
            continue
