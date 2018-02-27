from rest_framework import serializers

from .models import TweetInfo


class TweetInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetInfo
        fields = '__all__'
