# visualize_sentiment.py
# Chapter 6: Visualizing Sentiment Trends Over Time
# Twitter Data Mastery: From Zero to Dashboard in 7 Days

import tweepy
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

BEARER_TOKEN = "YOUR_BEARER_TOKEN"
client = tweepy.Client(bearer_token=BEARER_TOKEN)

query = '#Budget2025 lang:en -is:retweet'
analyzer = SentimentIntensityAnalyzer()
tweets = []
next_token = None

for i in range(5):
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

        date = tweet.created_at.date()
        tweets.append({'date': date, 'sentiment': sentiment})

    next_token = response.meta.get('next_token')
    if not next_token:
        break

df = pd.DataFrame(tweets)
df_grouped = df.groupby(['date', 'sentiment']).size().unstack(fill_value=0)

df_grouped.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Sentiment Trend on #Budget2025')
plt.ylabel('Tweet Count')
plt.xlabel('Date')
plt.tight_layout()
plt.savefig("chapter6_sentiment_trend.png")
plt.show()

