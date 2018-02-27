import csv

from django.http import Http404, HttpResponse
from rest_framework import pagination
from rest_framework.generics import ListAPIView

from twitter_api.models import TweetInfo
from twitter_api.serializers import TweetInfoSerializer


class SearchApi(ListAPIView):
    pagination.CursorPagination.ordering = '-created_at'
    serializer_class = TweetInfoSerializer

    def get_queryset(self):
        search_key = self.request.GET.get('search_key')
        if search_key is not None:
            results = TweetInfo.objects.filter(text__contains=search_key)
            return results
        raise Http404('Invalid search')

    def get(self, request, *args, **kwargs):
        self.format = request.GET.get('format', False)
        if self.request.GET.get('csv') is not None:
            print('download')
            return HttpResponse(download_csv(self.get_queryset()), content_type='text/csv')
        return super(SearchApi, self).get(request, *args, **kwargs)


class FilterApi(ListAPIView):
    pagination.CursorPagination.ordering = '-created_at'
    serializer_class = TweetInfoSerializer

    def get_queryset(self):
        text_search_key = self.request.GET.get('text_search_key')
        max_fav_tweet_count = self.request.GET.get('max_fav_tweet_count')
        min_fav_tweet_count = self.request.GET.get('min_fav_tweet_count')
        max_reply_tweet_count = self.request.GET.get('max_reply_tweet_count')
        min_reply_tweet_count = self.request.GET.get('min_reply_tweet_count')
        max_retweet_count = self.request.GET.get('max_retweet_count')
        min_retweet_count = self.request.GET.get('min_retweet_count')
        min_quote_count = self.request.GET.get('min_qot_count')
        max_quote_count = self.request.GET.get('max_qot_count')
        language = self.request.GET.get('lan')
        user_ends_with = self.request.GET.get('user_ew')
        user_starts_with = self.request.GET.get('user_sw')
        hashtag = self.request.GET.get('hash_tag')
        user_mentions = self.request.GET.get('user_men')
        min_user_favorite_count = self.request.GET.get('min_user_fav_count')
        max_user_favorite_count = self.request.GET.get('max_user_fav_count')
        min_user_followers_count = self.request.GET.get('min_user_fol_count')
        max_user_followers_count = self.request.GET.get('max_user_fol_count')
        min_user_friends_count = self.request.GET.get('min_user_frnd_count')
        max_user_friends_count = self.request.GET.get('max_user_frnd_count')
        screen_name_Starts_with = self.request.GET.get('srn_name_sw')
        screen_name_ends_with = self.request.GET.get('srn_name_ew')
        day = self.request.GET.get('day_e')
        max_day = self.request.GET.get('max_day')
        min_day = self.request.GET.get('min_day')

        results = TweetInfo.objects.all()

        is_filtered = False

        # text filter
        if text_search_key is not None:
            results = results.filter(text__contains=text_search_key)
            is_filtered = True

        # hashtag filter
        if hashtag is not None:
            results = results.filter(hash_tags__contains=hashtag)
            is_filtered = True

        # user mentions filter
        if user_mentions is not None:
            results = results.filter(user_mentions__contains=user_mentions)
            is_filtered = True
        # number of likes to tweet filter
        if min_fav_tweet_count is not None and bool(represents_int(min_fav_tweet_count)):
            results = results.filter(favorite_count__gte=min_fav_tweet_count)
            is_filtered = True
        if max_fav_tweet_count is not None and bool(represents_int(max_fav_tweet_count)):
            results = results.filter(favorite_count__lte=max_fav_tweet_count)
            is_filtered = True

        # number of reply to tweets count filter
        if max_reply_tweet_count is not None and bool(represents_int(max_reply_tweet_count)):
            results = results.filter(reply_count__lte=max_reply_tweet_count)
            is_filtered = True
        if min_reply_tweet_count is not None and bool(represents_int(min_reply_tweet_count)):
            results = results.filter(reply_count__gte=min_reply_tweet_count)
            is_filtered = True

        # number of retweets count filter
        if max_retweet_count is not None and bool(represents_int(max_retweet_count)):
            results = results.filter(retweet_count__lte=max_retweet_count)
            is_filtered = True
        if min_retweet_count is not None and bool(represents_int(min_retweet_count)):
            results = results.filter(retweet_count__gte=min_retweet_count)
            is_filtered = True

        # number of user likes filter
        if min_user_favorite_count is not None and bool(represents_int(min_user_favorite_count)):
            results = results.filter(user_favorite_count__gte=min_user_favorite_count)
            is_filtered = True
        if max_user_favorite_count is not None and bool(represents_int(max_user_favorite_count)):
            results = results.filter(user_favorite_count__lte=max_user_favorite_count)
            is_filtered = True

        # number of user followers filter
        if min_user_followers_count is not None and bool(represents_int(min_user_followers_count)):
            results = results.filter(user_followers_count__gte=min_user_followers_count)
            is_filtered = True
        if max_user_followers_count is not None and bool(represents_int(max_user_followers_count)):
            results = results.filter(user_followers_count__lte=max_user_followers_count)
            is_filtered = True

        # number of user friends filter
        if min_user_friends_count is not None and bool(represents_int(min_user_friends_count)):
            results = results.filter(user_friends_count__gte=min_user_friends_count)
            is_filtered = True
        if max_user_friends_count is not None and bool(represents_int(max_user_friends_count)):
            results = results.filter(user_friends_count__lte=max_user_friends_count)
            is_filtered = True

        # number of user friends filter
        if min_quote_count is not None and bool(represents_int(min_quote_count)):
            results = results.filter(user_friends_count__gte=min_quote_count)
            is_filtered = True
        if max_quote_count is not None and bool(represents_int(max_quote_count)):
            results = results.filter(user_friends_count__lte=max_quote_count)
            is_filtered = True

        # language filter
        if language is not None:
            results = results.filter(language=language)
            is_filtered = True

        # username filter
        if user_ends_with is not None:
            results = results.filter(user_name__endswith=user_ends_with)
            is_filtered = True
        if user_starts_with is not None:
            results = results.filter(user_name__startswith=user_starts_with)
            is_filtered = True

        # screen name filter
        if screen_name_ends_with is not None:
            results = results.filter(user_name__endswith=screen_name_ends_with)
            is_filtered = True
        if screen_name_Starts_with is not None:
            results = results.filter(user_name__startswith=screen_name_Starts_with)
            is_filtered = True

        # date filter
        if day is not None:
            results = results.filter(created_at__day=day)
            is_filtered = True
        if max_day is not None:
            results = results.filter(created_at__lte=max_day)
            is_filtered = True
        if min_day is not None:
            results = results.filter(created_at__gte=min_day)
            is_filtered = True

        if is_filtered:
            download_csv(results)
            return results
        raise Http404("Invalid filter")

    def get(self, request, *args, **kwargs):
        self.format = request.GET.get('format', False)
        if self.request.GET.get('csv') is not None:
            return HttpResponse(download_csv(self.get_queryset()), content_type='text/csv')
        return super(FilterApi, self).get(request, *args, **kwargs)


def represents_int(i):
    try:
        int(i)
        return True
    except (TypeError, ValueError):
        return False


def download_csv(data):
    field_names = ['user_name', 'screen_name', 'language', 'user_favorite_count', 'user_friends_count', 'user_followers_count', 'quote_count',
                   'reply_count', 'retweet_count', 'favorite_count', 'hash_tags_count', 'user_mentions_count']
    response = HttpResponse(content_type='text/csv')
    # force download.
    response['Content-Disposition'] = 'attachment;filename=export.csv'
    writer = csv.writer(response)
    writer.writerow(field_names)
    # Write data rows
    for obj in data:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response
