import re
from nltk.stem import WordNetLemmatizer
import nltk
import pandas as pd
import preprocessor as p
from wordsegment import segment, load
from bs4 import BeautifulSoup

contraction_dict = {"ain't": "is not", "aren't": "are not", "can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not", "didn't": "did not",  "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not", "he'd": "he would", "he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",  "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have", "I'm": "I am", "I've": "I have", "i'd": "i would", "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have", "i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would", "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have", "it's": "it is", "let's": "let us", "ma'am": "madam", "mayn't": "may not", "might've": "might have", "mightn't": "might not", "mightn't've": "might not have", "must've": "must have", "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have", "o'clock": "of the clock", "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have", "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is", "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have","so've": "so have", "so's": "so as", "this's": "this is", "that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would", "there'd've": "there would have", "there's": "there is", "here's": "here is", "they'd": "they would", "they'd've": "they would have", "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have", "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are", "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",  "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is", "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have", "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have", "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would", "y'all'd've": "you all would have", "y'all're": "you all are", "y'all've": "you all have", "you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have", "you're": "you are", "you've": "you have"}

def preprocess_text(text, flg_stemm=False, flg_lemm=True, lst_stopwords=None):

  #Tokenise & clean
  text = p.clean(text) # removes mentions, numbers, emojis, URLS 
  text = BeautifulSoup(text, features = "lxml").get_text()  # converts HTML entities 
  text = replace_contractions(text) # contractions are extended, e.g isn't = is not 
  text = text.translate(str.maketrans(' ', ' ', punctuation)) # punctuation (except for #) removed

  lst_text = text.split() # split into a list
  lst_text = sep_hashtags(lst_text) # hashtags are separated into words

  #remove Stopwords
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

def sep_hashtags(tweet):

  sep_hashtags = []
  for word in tweet:
    if word[0] == '#':
      cleaned_hashtag = segment(word)
      for segmented in cleaned_hashtag:
        sep_hashtags.append(segmented)
    else:
      sep_hashtags.append(word)
  return sep_hashtags

def get_contractions(contraction_dict):
    contraction_re = re.compile('(%s)' % '|'.join(contraction_dict.keys()))
    return contraction_dict, contraction_re

def replace_contractions(text):
    def replace(match):
        return contractions[match.group(0)]
    return contractions_re.sub(replace, text)


load()
punctuation = "+!?$%&()*+,'-./:;<=>[\]^_`{|}~@\""
contractions, contractions_re = get_contractions(contraction_dict)
p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.NUMBER, p.OPT.EMOJI)

airline_stopwords = ["United", "AmericanAir", "USAirways", "JetBlue", "VirginAmerica",
                     "SouthwestAir"]

df = pd.read_csv('Tweets.csv')
df["text"] = df["text"].apply(lambda x: preprocess_text(
    x, flg_lemm=True, lst_stopwords=airline_stopwords))

df.to_csv("ProcessedTweets.csv")
