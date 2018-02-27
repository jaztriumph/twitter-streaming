import json

from django.db import models
from django.utils import timezone


class TweetInfo(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=5000)
    created_at = models.DateTimeField(default=timezone.now)
    user_name = models.TextField(max_length=100)
    user_favorite_count = models.IntegerField()
    user_friends_count = models.IntegerField()
    user_followers_count = models.IntegerField()
    screen_name = models.TextField(max_length=100)
    language = models.CharField(max_length=100)
    quote_count = models.IntegerField()
    reply_count = models.IntegerField()
    retweet_count = models.IntegerField()
    favorite_count = models.IntegerField()
    hash_tags = models.TextField(max_length=1000, default='')
    user_mentions = models.TextField(max_length=1000, default='')

    def set_hashtags(self, x):
        self.hash_tags = json.dumps(x)

    def get_hashtags(self):
        return json.loads(self.hash_tags)

    def set_user_mentions(self, x):
        self.user_mentions = json.dumps(x)

    def get_user_mentions(self):
        return json.loads(self.user_mentions)
