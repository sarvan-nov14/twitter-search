"""
Helper functions
"""
import twitter

from django.conf import settings


def authenticate_with_twitter():

    """Make authentication with twitter"""

    twitter_api = twitter.Api(consumer_key=settings.CONSUMER_API_KEY,
                              consumer_secret=settings.CONSUMER_API_KEY_SECRET,
                              access_token_key=settings.ACCESS_TOKEN,
                              access_token_secret=settings.ACCESS_TOKEN_SECRET
                              )

    return twitter_api


