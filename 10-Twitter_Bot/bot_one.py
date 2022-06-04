"""
Programmer: Sam Skywalker
Purpose: Exploration
Dte: 12022.05.24.16:05
"""

import tweepy

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


# I don't wanna do this project because, I use twitter, I respect twitter & I know how much we hate bots on twitter...
