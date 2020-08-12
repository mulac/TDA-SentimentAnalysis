import re
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords
import pandas as pd


def preprocess_text(text, flg_stemm=False, flg_lemm=True, lst_stopwords=None):

  #Clean
  text = re.sub(r'[^\w\s]', '', str(text).lower().strip())

  #Tokenise
  lst_text = text.split()

  #remove Stopwords
  if lst_stopwords is not None:
    lst_text = [word for word in lst_text if word not in lst_stopwords]

  #Stemming
  if flg_stemm:
    ps = nltk.stem.porter.PorterStemmer()
    lst_text = [ps.stem(word) for word in lst_text]

  #Lemmatisation
  if flg_lemm:
    lem = nltk.stem.wordnet.WordNetLemmatizer()
    lst_text = [lem.lemmatize(word) for word in lst_text]

  #rejoin the string
  text = " ".join(lst_text)
  return text


lst_stopwords = nltk.corpus.stopwords.words("english")
airline_stopwords = ["united", "americanair", "usairways", "jetblue", "virginamerica",
                      "southwestair", "thanks", "thnx", "thank you", "flight", "thank", "get", "please", "u"]
for stopword in airline_stopwords:
  lst_stopwords.append(stopword)
  
df = pd.read_csv('Tweets.csv')
df["text"] = df["text"].apply(lambda x: preprocess_text(
    x, flg_lemm=True, lst_stopwords=lst_stopwords))

df.to_csv("ProcessedTweets.csv")
