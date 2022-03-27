# You will need to PIP INSTALL tweepy for this to work and also create a twitter API. Run this on your own machine.

import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)  # prints your name.
print(user.screen_name)
# print(user.followers_count)​
search = "kylesm11th"
numberOfTweets = 5


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)

# Be nice to your followers. Follow everyone!

# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    # if follower.name == 'Usernamehere':
        # print(follower.name)
        # follower.follow()


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# fetches user and shows last 20 followers!
user = api.get_user("kylesm11th")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)


# tweet update status
#api.update_status("Python Tweet")
