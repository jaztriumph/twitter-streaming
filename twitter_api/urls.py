from django.conf.urls import url

from twitter_streaming.celery import startup
from . import views

app_name = 'twitter_api'
urlpatterns = [
    url(r'^search/$', views.SearchApi.as_view(), name='search'),
    url(r'^filter/$', views.FilterApi.as_view(), name='search'),
]
startup.delay()
