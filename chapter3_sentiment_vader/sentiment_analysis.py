# sentiment_analysis.py
# Chapter 3: Unlocking the Power of Sentiment Analysis with VADER
# Twitter Data Mastery: From Zero to Dashboard in 7 Days

import tweepy
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# STEP 1: Authentication
BEARER_TOKEN = "YOUR_BEARER_TOKEN_HERE"
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# STEP 2: Define your query
query = '#IndianEconomy lang:en -is:retweet'

# STEP 3: Fetch tweets
response = client.search_recent_tweets(
    query=query,
    tweet_fields=['created_at', 'text'],
    max_results=50
)


# STEP 4: Setup Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# STEP 5: Analyze and store tweets

tweets = []
for tweet in response.data:
    text = tweet.text
    score = analyzer.polarity_scores(text)['compound']

    if score >= 0.05:
        sentiment = "Positive"
    elif score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    tweets.append({'text': text, 'sentiment': sentiment})


# STEP 6: Save to CSV

df = pd.DataFrame(tweets)
df.to_csv("chapter3_sentiment.csv", index=False)
print("Sentiment-labeled tweets saved!")