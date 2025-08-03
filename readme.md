# 🐦 Twitter Data Mastery: From Zero to Dashboard in 7 Days

Welcome to the official repository for the book **"Twitter Data Mastery: From Zero to Dashboard in 7 Days"** — your complete, hands-on guide to mastering the Twitter API with Python, sentiment analysis, and interactive dashboards using Streamlit.

> 💡 **For:** Beginners, data journalists, political analysts, social media researchers, and aspiring data scientists.

---

## 📚 What You’ll Learn

✅ Fetch real tweets using the Twitter (X) API  
✅ Understand endpoints, tweet fields, expansions, user info  
✅ Perform sentiment analysis using VADER  
✅ Visualize tweet trends using `matplotlib` and `pandas`  
✅ Build real-time dashboards using Streamlit  
✅ Export tweet data and summaries in CSV format  
✅ Bonus: Pagination, summary stats, date filtering and more!

---

## 🧭 Project Structure (Chapterwise Code)

```plaintext
twitter-data-mastery/
│
├── chapter1_first_fetch/
│   └── fetch_tweets.py
│
├── chapter2_user_expansion/
│   └── user_expansion.py
│
├── chapter3_sentiment_vader/
│   └── sentiment_analysis.py
│
├── chapter4_visualization/
│   └── sentiment_plot.py
│
├── chapter5_pagination/
│   └── fetch_paginated.py
│
├── chapter6_sentiment_trend/
│   └── sentiment_trend.py
│
├── chapter7_streamlit_dashboard/
│   └── dashboard.py
│
├── chapter8_summary_stats/
│   └── summary_export.py
│
└── README.md  ← You are here!

git clone https://github.com/adminravi/twitter-data-mastery.git
cd twitter-data-mastery


pip install -r requirements.txt


You’ll need:

tweepy

pandas

matplotlib

vaderSentiment

streamlit

3. Setup Your Twitter API Credentials
Get a Bearer Token from developer.x.com and insert it in your scripts:

client = tweepy.Client(bearer_token="YOUR_BEARER_TOKEN")


Run the Streamlit Dashboard
Navigate to the dashboard chapter and run:

cd chapter7_streamlit_dashboard
streamlit run dashboard.py

Cheatsheets Included
Check the Twitter API Cheatsheets.docx for:

tweet_fields, user_fields, media_fields, place_fields

expansions

Query filters and operators

Endpoint references


💡 Why This Book is Different
This project is part of a bigger learning movement to:

Teach data science through real-world tools

Connect coding with journalism, politics, and activism

Bridge beginner learning with production-level skills

With Da Vinci mindset and Bhai Gyaan tips, we believe you’ll build more than just scripts — you’ll build confidence and real tools.

📖 Get the Book
Coming soon on Amazon.
Stay tuned for the official launch date!

Credits
Author & Developer: Ravi Verma

📬 Feedback
Have suggestions, feedback, or want to collaborate?

Drop a mail (adminravi@gmail.com) or raise an issue in this repo.

Star this repo if you found it helpful!
