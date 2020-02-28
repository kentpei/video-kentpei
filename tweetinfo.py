#!/usr/bin/env python
# encoding: utf-8
import re
import json
import tweepy  # https://github.com/tweepy/tweepy
import os
import configparser
import shutil
shutil.copy('keys','keys.py')
from keys import *

# Twitter API credentials
def get_oldJson(name):
  text = []
  with open('jsonFolder/' + name + '.json') as json_data:
      data_dict = json.load(json_data)
      emoji_pattern = re.compile("["
                                 u"\U0001F600-\U0001F64F"  # emoticons
                                 u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                 u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                 u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                 "]+", flags=re.UNICODE)
  for line in data_dict:
      line = emoji_pattern.sub(r'', line)
      text.append(line)
  return text

def get_all_tweets(name,n):
    # Here for testing keys exist or not
    try:
        f = open('keys') #wrong name or file not exist will return the json file
        print('keys open')
        f.close()
    except IOError:
        print("File error")
        return get_oldJson(name)
    # check for whether keys file is empty or not first
    if (os.stat('keys').st_size <= 0):
        print('No content in the key file')
        # call function for saved json file
        return get_oldJson(name)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=name, count=n)
    for tweet in new_tweets:
        alltweets = alltweets + [tweet.text]
    return alltweets
