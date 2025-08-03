# dashboard.py
# Chapter 8: Summary Stats and Export Tools
# Twitter Data Mastery: From Zero to Dashboard in 7 Days

import streamlit as st
import tweepy
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# SETUP
BEARER_TOKEN = "YOUR_BEARER_TOKEN_HERE"
client = tweepy.Client(bearer_token=BEARER_TOKEN)
analyzer = SentimentIntensityAnalyzer()

# STREAMLIT UI
st.title("Twitter Sentiment Dashboard")
query = st.text_input("Enter your hashtag or keyword:", "#IndianEconomy")

if st.button("Fetch Tweets"):
    with st.spinner("Fetching recent tweets..."):
        response = client.search_recent_tweets(
            query=f"{query} lang:en -is:retweet",
            tweet_fields=['created_at', 'text', 'public_metrics'],
            max_results=50
        )

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

            tweets.append({
                'time': tweet.created_at,
                'text': text,
                'likes': tweet.public_metrics['like_count'],
                'retweets': tweet.public_metrics['retweet_count'],
                'replies': tweet.public_metrics['reply_count'],
                'sentiment': sentiment
            })

        df = pd.DataFrame(tweets)

        st.success("Tweets fetched and analyzed!")

        # DISPLAY TABLE
        st.write("### Tweet Data")
        st.dataframe(df)

        # SUMMARY STATS
        st.write("### Summary Stats")
        st.write(f"Total Tweets Fetched: {len(df)}")
        score_avg = df['text'].apply(lambda x: analyzer.polarity_scores(x)['compound']).mean()
        st.write(f"Average Sentiment Score: {score_avg:.2f}")

        # EXPORT BUTTONS
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download All Tweets as CSV", csv, "all_tweets.csv", "text/csv")

        summary_df = df['sentiment'].value_counts().reset_index()
        summary_df.columns = ['Sentiment', 'Count']
        csv_summary = summary_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Sentiment Summary", csv_summary, "sentiment_summary.csv", "text/csv")

        # BONUS: Filter & Export Positive Tweets
        positive_df = df[df['sentiment'] == "Positive"]
        csv_positive = positive_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Positive Tweets Only", csv_positive, "positive_tweets.csv", "text/csv")

