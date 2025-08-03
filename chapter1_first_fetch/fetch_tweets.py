# fetch_tweets.py
# Chapter 1: Your First Tweet Fetcher
# Twitter Data Mastery: From Zero to Dashboard in 7 Days

import tweepy
import pandas as pd

# STEP 1: Replace with your own Bearer Token. 
# To create your free Bearer Token go to: https://developer.x.com/en/portal/products/free
BEARER_TOKEN = "PASTE_YOUR_BEARER_TOKEN_HERE"

# STEP 2: Set up Tweepy client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# STEP 3: Define your search query
query = "#IndianEconomy lang:en -is:retweet"

# STEP 4: Fetch 10 recent tweets using Twitter API v2
response = client.search_recent_tweets(
    query=query,
    tweet_fields=['created_at', 'text'],
    max_results=10
)

# STEP 5: Extract tweet content
tweets = []
for tweet in response.data:
    tweets.append({
        "created_at": tweet.created_at,
        "text": tweet.text
    })

# STEP 6: Save to CSV
df = pd.DataFrame(tweets)
df.to_csv("chapter1_tweets.csv", index=False)

print("10 tweets saved to chapter1_tweets.csv")