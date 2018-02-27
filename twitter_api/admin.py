from django.contrib import admin

from twitter_api.models import TweetInfo


@admin.register(TweetInfo)
class TweetInfoAdmin(admin.ModelAdmin):
    def user_name(self, obj):
        return obj.user_name

    user_name.short_description = 'user name'

    def screen_name(self, obj):
        return obj.screen_name

    screen_name.short_description = 'screen name'

    def language(self, obj):
        return obj.language

    language.short_description = 'language'

    def time(self, obj):
        return obj.created_at.strftime('%I:%M:%S - %d %b %y')

    time.admin_order_field = "client_time"

    def retweet_count(self, obj):
        return obj.retweet_count

    retweet_count.admin_order_field = "retweet_count"

    def tweet_text(self, obj):
        return obj.text

    def hashtags(self, obj):
        return obj.hash_tags

    def reply_count(self, obj):
        return obj.reply_count

    list_display = ['user_name', 'screen_name', 'text', 'user_mentions']
