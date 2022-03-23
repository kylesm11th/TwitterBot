# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    consumer_key = '9Z1j0ncIYxHJaS3pfI3ucKXLm'
    consumer_secret = 'TVsThRM55MDtVGCfrQ7idzWvJfzYemD6VsNFmnFLBTQNZC9hAo'
    access_token = '20374346-0wYgdjpsOgGhlQfQQjHr3o8YLA3uhAfL7xp1GXrw4'
    access_token_secret = 'Nyc4NLmowZbRhDn7gnNnV0YIDFrdrfIeEUKACA3YcJcsd'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
