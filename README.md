 # twitter-streaming
   search and filter from a stream of twitter tweets

 # Built with
 * [Django](https://www.djangoproject.com/) - Web framework used
 * [Celery](http://docs.celeryproject.org) - Used to run back ground tasks

 ## Get Started

 Start the server as usual in django then run the command
 `celery -A twitter_streaming worker --loglevel=info` in your terminal to run and see logs of celery backgroung task.

 To know more read [here](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)

 ## API Usage

 ### Search API
 `api/search/?search_key=<your_search_key>`

 this gives the tweets according to 'your_search_key' in pages of maxiumum of 20 tweets each.
 
 Example:
 when running in local server `http://localhost:8000/api/search/?search_key=good`
 
 
 Json Response:  ```{
    "next": "http://localhost:8000/api/search/?cursor=cD0yMDE4LTAyLTI3KzE3JTNBNTclM0EwMyUyQjAwJTNBMDA%3D&search_key=good",
    "previous": null,
    "results": [
        {
            "id": 8252,
            "text": "RT @Mr_Hardey: When the president and his fans are talking about how good he has performed and how aggressive he's treating the crisis of b…",
            "created_at": "2018-02-27T23:37:22+05:30",
            "user_name": "HEADmaster",
            "user_favorite_count": 1997,
            "user_friends_count": 5340,
            "user_followers_count": 11261,
            "screen_name": "Mr_Hardey",
            "language": "en",
            "quote_count": 0,
            "reply_count": 0,
            "retweet_count": 0,
            "favorite_count": 0,
            "hash_tags": "[]",
            "user_mentions": "[\"HEADmaster\"]"
        },..........]```
 
 In the response previous and next url contains link for next amd previous data and results contains tweets information
 
 ----------------------------------------
 ### Filter API
 
 `api/filter/?user_ew=<user_name_ends_with_key>&min_user_fav_count=<min_number_of_favourites_user_must_have>`
 
filter has many fields listed below:

          keys                                         filter information
    'text_search_key'                         searches for specified key in text of tweet
    'lan'                                     returns tweets with specific language
    'day'                                     returns tweets on that specific date.Format should be yyyy-mm-dd(year-monthday)
    'max_day'                                 returns tweets until that specified date
    'min_day'                                 returns tweets after that specified date
    'user_ew'                                 returns tweets with username ending with specified string
    'user_sw'                                 returns tweets with username starting with specified string
    'srn_name_ew'                             returns tweets with screenname ending with specified string
    'srn_name_sw'                             returns tweets with screenname starting with specified string
    'hash_tag'                                 returns tweets which contains specified hashtag
    'user_men'                                returns tweets which contains mentions of specified username
    'max_fav_tweet_count'                     return tweets with less favorite count than this
    'min_fav_tweet_count'                     return tweets with more favorite count than this
    'max_reply_tweet_count'                   return tweets with number of replies less than this
    'min_reply_tweet_count'                   return tweets with number of replies more than this
    'max_retweet_count'                       return tweets with number of retweets less than this
    'min_retweet_count'                       return tweets with number of retweets more than this
    'max_qot_count'                           return tweets with number of quotes less than this
    'min_qot_count'                           return tweets with number of quotes more than this
    'max_user_fav_count'                      return tweets with user favorites less than this
    'min_user_fav_count'                      return tweets with user favorites more than this
     'max_user_fol_count'                      return tweets with user followers less than this
    'min_user_fol_count'                      return tweets with user followers more than this
    'max_user_frnd_count'                     return tweets with user friends less than this
    'min_user_frnd_count'                     return tweets with user friends more than this

 Example:
 
 `http://localhost:8000/api/filter/?lan=en&?min_retweet_count=500&?user_sw='joh'`
 
 the above request returns tweets in english with username starting with 'joh' and with retweets greater than 500.
 
 for language code see [here](https://www.loc.gov/standards/iso639-2/php/code_list.php).
 
