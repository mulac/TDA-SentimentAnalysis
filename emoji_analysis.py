from emosent import get_emoji_sentiment_rank


def get_sentiment(emoji):
    return get_emoji_sentiment_rank(emoji)['sentiment_score']


def get_unicode_name(emoji):
    return get_emoji_sentiment_rank(emoji)['unicode_name']

