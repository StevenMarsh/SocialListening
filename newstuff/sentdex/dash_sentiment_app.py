#ANALYZING TWITTER.DB TWEETS
import sqlite3
import pandas as pd

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

#order by unix so date
df = pd.read_sql("SELECT * FROM sentiment WHERE tweet ORDER BY unix DESC LIMIT 1000", conn)

#want time to be in order we want. column we want to sort by: unix. 
df.sort_values('unix',inplace=True)
#SMOOTH SENTIMENT VALUES FOR VISUALIZATION WITH ROLLING AVERAGE. 
#specify legnth of rolling average
df['Smoothed_Sentiment']=df['sentiment'].rolling(int(len(df)/5)).mean()
df.dropna(inplace=True)

print(df.tail())