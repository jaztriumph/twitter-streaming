# Generated by Django 2.0.2 on 2018-02-27 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetinfo',
            name='hash_tags_count',
            field=models.IntegerField(default=0),
        ),
    ]
