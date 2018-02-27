# from celery import Celery
# from tweepy import OAuthHandler
# from tweepy import Stream
# from tweepy.streaming import StreamListener
#
# app = Celery('tasks', broker='pyamqp://guest@localhost//')
# # Variables that contains the user credentials to access Twitter API
# access_token = "817355436995190785-9NNNFpwhtQRxZJUAWHCXDZLzqNfQ3Dq"
# access_token_secret = "JTpYExcLDllGARXsHOgJrkVvFCTJcbdEGb4acwPZq7wFt"
# consumer_key = "9czzvO7F3m5eJHdJ6dMAs0ZhW"
# consumer_secret = "RZicUxfALTnG4bRmSof2b0o95Xc1bijZ0fOTw8rmUAAACET2ep"
#
#
# # This is a basic listener that just prints received tweets to stdout.
# class StdOutListener(StreamListener):
#
#     def on_data(self, data):
#         print(data)
#         return True
#
#     def on_error(self, status):
#         print(status)
#
#
# # if __name__ == '__main__':
# #     # This handles Twitter authentication and the connection to Twitter Streaming API
# #     l = StdOutListener()
# #     auth = OAuthHandler(consumer_key, consumer_secret)
# #     auth.set_access_token(access_token, access_token_secret)
# #     stream = Stream(auth, l)
#
# @app.task()
# def startup():
#     l = StdOutListener()
#     auth = OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#     stream = Stream(auth, l)
#     try:
#         stream.sample()
#     except Exception:
#         print("exception")
#     print("Started")
#
#
# startup()
# # print("Started")
