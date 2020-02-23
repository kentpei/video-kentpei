#!/usr/bin/env python
# encoding: utf-8


import tweepy  # https://github.com/tweepy/tweepy

# Twitter API credentials
consumer_key = 'OPXVWM0pzdkiOWzvwZKwNjffb'
consumer_secret = '0PlU0H4wLc6bh7Q0GAZN2ms3Tf6a6aQCTRkj7GybBWOoL4yyUH'
access_key = '1171846283398537216-5XyhwpSZGKJo1WA7CvPwI0oCSPQlty'
access_secret = 'mdYZBzjp3P6tqreWrgNMTqeTyKMIzvIhlpBWKqVhaqlLm'


def get_all_tweets(name,n):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=name, count=n)
    for tweet in new_tweets:
        alltweets = alltweets + [tweet.text]
    return alltweets

