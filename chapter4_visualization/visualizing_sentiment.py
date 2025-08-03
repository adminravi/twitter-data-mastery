# visualizing_sentiment.py
# Chapter 4: Visualizing Sentiment — Bringing Tweets to Life
# Twitter Data Mastery: From Zero to Dashboard in 7 Days

import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Load the sentiment CSV
df = pd.read_csv("chapter3_sentiment.csv")

# STEP 2: Count each sentiment
sentiment_counts = df['sentiment'].value_counts()

# STEP 3: Create a bar chart
sentiment_counts.plot(kind='bar', color=['green', 'blue', 'red'])
plt.title("Sentiment Analysis of Tweets")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.xticks(rotation=0)

# STEP 4: Show and save the plot
plt.tight_layout()
plt.savefig("chapter4_sentiment_chart.png")
plt.show()

