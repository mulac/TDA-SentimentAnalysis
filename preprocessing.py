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





