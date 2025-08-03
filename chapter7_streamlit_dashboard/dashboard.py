# dashboard.py
# Chapter 7: Building a Real-Time Sentiment Dashboard with Streamlit
# Twitter Data Mastery: From Zero to Dashboard in 7 Days

import streamlit as st
import tweepy
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


BEARER_TOKEN = "YOUR_BEARER_TOKEN"
client = tweepy.Client(bearer_token=BEARER_TOKEN)
analyzer = SentimentIntensityAnalyzer()

st.title("Twitter Sentiment Dashboard")
hashtag = st.text_input("Enter hashtag (without #)", "IndianEconomy")

query = f'#{hashtag} lang:en -is:retweet'
tweets = []
response = client.search_recent_tweets(
    query=query,
    tweet_fields=['created_at', 'text'],
    max_results=50
)

for tweet in response.data:
    score = analyzer.polarity_scores(tweet.text)['compound']
    if score >= 0.05:
        sentiment = "Positive"
    elif score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    tweets.append({
        'time': tweet.created_at,
        'text': tweet.text,
        'sentiment': sentiment
    })


df = pd.DataFrame(tweets)
st.write("### Sentiment Breakdown")
st.dataframe(df[['sentiment']].value_counts().reset_index(name='count'))

st.write("### Tweets Table")
st.dataframe(df[['time', 'text', 'sentiment']])

st.write("### Sentiment Pie Chart")
st.pyplot(
    df['sentiment'].value_counts().plot.pie(autopct='%1.0f%%', figsize=(6, 6)).figure
)