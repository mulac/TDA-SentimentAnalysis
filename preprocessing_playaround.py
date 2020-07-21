from pandas import DataFrame, read_csv
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from wordsegment import segment, load

load()

def check_word(word):
    if word not in stopwords and word.isalpha():
        cleaned_tweet.append(word)

stopwords = set(stopwords.words('english'))
tweet_data = read_csv("Tweets.csv")
tokeniser = TweetTokenizer(preserve_case=False)

for tweet in tweet_data['text']:
    
    tweet = tokeniser.tokenize(tweet)
    cleaned_tweet = list()

    for i in range(len(tweet))  :

        word = tweet[i]

        if word[0] == "#":

            split_hashtag = segment(word)
            if split_hashtag != []:

                for split_word in split_hashtag:
                    check_word(split_word)
        else:
            check_word(word)

    tweet = cleaned_tweet
    print(tweet)


## emojis, punctuation, mentions, links removed
## hashtags are split into words
## stopwords removed 
## lowercase 

## maybe emojis could be kept? 