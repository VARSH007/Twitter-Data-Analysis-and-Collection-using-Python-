import tweepy
import pandas as pd
import json
from datetime import datetime

# we will get all the keys & secret_keys from https://developer.twitter.com/en
access_key = " "
access_secret = " "
consumer_key = " "
consumer_secret = " "

# Set up the API connection
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Get the user's tweets
tweets = api.user_timeline(screen_name='@elonmusk', count=200, include_rts=False, tweet_mode='extended')

# Create a list of dictionaries for each tweet
tweet_list = [{"user": tweet.user.screen_name, "text": tweet._json["full_text"], "favorite_count": tweet.favorite_count, "retweet_count": tweet.retweet_count, "created_at": tweet.created_at} for tweet in tweets]

# Create a Pandas DataFrame from the list of dictionaries
df = pd.DataFrame(tweet_list)

# Save the DataFrame to a CSV file
df.to_csv('refined_tweets.csv')
