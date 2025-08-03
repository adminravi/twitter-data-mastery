# pagination.py
# Chapter 5: Pagination — Breaking Twitter’s 100-Tweet Barrier
# Twitter Data Mastery: From Zero to Dashboard in 7 Days

import tweepy
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Step 1
BEARER_TOKEN = "YOUR_BEARER_TOKEN"
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Step 2
query = '#Elections2025 lang:en -is:retweet'
analyzer = SentimentIntensityAnalyzer()

# Step 3
tweets = []
next_token = None
pages = 3  # number of pages you want

for i in range(pages):
    print(f"Fetching page {i+1}...")
    response = client.search_recent_tweets(
        query=query,
        tweet_fields=['created_at', 'text'],
        max_results=100,
        next_token=next_token
    )

    for tweet in response.data:
        score = analyzer.polarity_scores(tweet.text)['compound']
        if score >= 0.05:
            sentiment = "Positive"
        elif score <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        tweets.append({'text': tweet.text, 'sentiment': sentiment})

    meta = response.meta
    next_token = meta.get('next_token')
    if not next_token:
        print("No more pages to fetch.")
        break


df = pd.DataFrame(tweets)
df.to_csv("chapter5_paginated_tweets.csv", index=False)
print("All tweets saved!")


