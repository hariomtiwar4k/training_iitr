# -*- coding: utf-8 -*-
"""Day 6 - Twitter Sentiment Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UyJ1tFwhXlVbt_lMJZ_ezjQTywEFi6Wr
"""

API_key = "dHrdynuzZJVyO2U9wmBcuRDq4"

API_secret_key =  "yjQCeGDR6WtIgwjzCyOHRUzAohTe4M7b1RGEvvvDO5E0HnqJlm"

Access_token = "182925782-T7j2WeXuOHXCpt80Y6engE5E6wPkAWM3dLpbNMDJ"

Access_token_secret = "NFgOWqjE2TTrHmI4PkX9ilMvkgdYarKFryC2vMUzUJXTB"

import tweepy  ### twitter api
from textblob import TextBlob  ### sentiment analysis

auth = tweepy.OAuthHandler(API_key,API_secret_key)

auth.set_access_token(Access_token,Access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Narendra Modi")

public_tweets

public_tweets[0].text

score = TextBlob(public_tweets[0].text)
score.sentiment

import pandas as pd
df = pd.DataFrame()

tweets = []
for i in public_tweets:
  tweets.append(i.text)
df['Tweets'] = tweets
df

sentiment = []
for i in public_tweets:
  s = (TextBlob(i.text)).sentiment
  sentiment.append(s)
df['Sentiments'] = sentiment
df

score = []
for i in public_tweets:
  s = (TextBlob(i.text)).sentiment
  if s[0]>0:
    score.append("Postive")
  elif s[0]<0:
    score.append("Negative")
  else:
    score.append("Neutral")
df['Score'] = score

df

