# fetch_with_users.py
# Chapter 2: Know Who Tweeted — User Expansions
# Twitter Data Mastery: From Zero to Dashboard in 7 Days

import tweepy
import pandas as pd

# STEP 1: Auth
BEARER_TOKEN = "YOUR_BEARER_TOKEN_HERE"
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# STEP 2: Query
query = '#IndianEconomy lang:en -is:retweet'

# STEP 3: Fetch tweets + user expansion
response = client.search_recent_tweets(
    query=query,
    tweet_fields=['created_at', 'text'],
    expansions=['author_id'],
    user_fields=['username', 'public_metrics'],
    max_results=10
)

# STEP 4: Map user info
users = {u['id']: u for u in response.includes['users']}

# STEP 5: Process
results = []
for tweet in response.data:
    user = users[tweet.author_id]
    results.append({
        'time': tweet.created_at,
        'tweet': tweet.text,
        'username': user.username,
        'followers': user.public_metrics['followers_count']
    })

# STEP 6: Save
pd.DataFrame(results).to_csv("chapter2_tweets_with_users.csv", index=False)
print("Saved to chapter2_tweets_with_users.csv")