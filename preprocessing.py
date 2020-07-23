from nltk.stem import WordNetLemmatizer

import pandas as pd
lemmatizer = WordNetLemmatizer()

def lement(str):
    return ' '.join([lemmatizer.lemmatize(word) for word in str.split()])

df = pd.read_csv('Tweets.csv')

for index, row in df.head(n = 15).iterrows():
    tweetText = " ".join(filter(lambda x: x[0] != '#' and x[0:4] != 'http' and x[0] != '&' and x[0] != '@', row['text'].split()))
    print("Tweet : " + str(index) + "\nOriginal\n" + tweetText + "\nLemmented\n"+ lement(tweetText))






