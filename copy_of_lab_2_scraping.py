# -*- coding: utf-8 -*-
"""Copy of Lab 2 - Scraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kIZlo7uMTd9YJqqoKGokd6crlgOWoxf-
"""

import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.in/Test-Exclusive-746/product-reviews/B07DJHXTLJ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
names = soup.find_all('span',class_='a-profile-name')[2:]
cust_name = [val.get_text() for val in names]
rating = soup.find_all('span',class_='a-icon-alt')[3:]
cust_rating = [val.get_text() for val in rating]
title=soup.select('a.review-title span')
titles = [val.get_text() for val in title]
date = soup.find_all('span',class_='review-date')[2:]
dates = [val.get_text() for val in date]
review=soup.select('span.review-text span')
reviews = [val.get_text() for val in review]

import pandas as pd
df = pd.DataFrame()
df["Date"] = dates
df['Customer Name'] = cust_name
df['Title'] = titles
df["Ratings"] = cust_rating
df['Review'] = reviews
df
