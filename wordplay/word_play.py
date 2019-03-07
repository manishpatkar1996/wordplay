# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 01:23:56 2019

@author: MANISH PATKAR
"""
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


consumer_key ='VOPVIExPhQsPhs6GUEU0WpKWO'
consumer_secret ='OYKzv48M97nrMrtZXkd0ATrwA4FNNQRRn7xogtnz4z9WA9YU1T'

access_token = '2807065872-lMvfJzjYGHiDUkcB3ZAMtID3Ebd66udBuYCTd7D'
access_token_secret = 'KV4njzTWFHrX5L0h4kjk1eL9Lq6haKbM6Olxv4QS47566'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token , access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('pulwama')
#col = ['CONTENT']                          
df = pd.DataFrame({'CONTENT':public_tweets})
df['CONTENT'] = df['CONTENT'].apply(lambda i : TextBlob(i).noun_phrase)




#df = pd.read_csv(r"Youtube04-Eminem.csv",encoding = 'latin-1' )

commentwords = " "
stopwords = set(STOPWORDS)

for val in df.CONTENT:
    val = str(val)
    tokens = val.split()
    
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        
    for word in tokens:
        commentwords = commentwords + word + ' '
        

wordcloud = WordCloud(width= 800, height= 800, background_color = 'white',stopwords= stopwords,min_font_size =10).generate(commentwords)

plt.figure(figsize = (4, 4), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 