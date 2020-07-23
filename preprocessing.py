import re
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords
import pandas as pd

stop_words = set(stopwords.words('english')) 

lemmatizer = WordNetLemmatizer()

def lement(str):
    return ' '.join([lemmatizer.lemmatize(word) for word in str.split()])

def removeStopwords(str):
    return ' '.join([w for w in str.split() if not w in stop_words])

df = pd.read_csv('Tweets.csv')
print(df)
for index, row in df.head(n = 15).iterrows():
    tweetText = " ".join(map(lambda x: x.lower(), filter(lambda x: x[0] != '#' and x[0:4]
         != 'http' and x[0] != '&' and x[0] != '@', row['text'].split())))
    print("Tweet : " + str(index) + "\nOriginal\n" + tweetText + "\nLemmented\n"+
         lement(tweetText) + "\nStop words removed\n" + removeStopwords(lement(tweetText)))

#Preprocessing

#UNICODE
#:) :D :-)
#Most offen emogis
#https://pypi.org/project/emosent-py/
#LOL, ikr, ttyl

#SOOOO AMAZINGGG


#

#Picking out uppercase. -> Emphasis
#Exclamation marks.     -> Emphasis 
#Time of year Negativity
#Dates where there negative
#Date ranges
#Bag of words, most used words to describe the airline.
#Best things -Customer service   -Rate them
#Worst things      
#PRICE, SPEED, CANCELLEND, DELAYED

# Ranking words appearing. predicting target audience.






