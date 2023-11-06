"""Lab 9"""
"""author - Avipreet Singh
   last modified - 10 november 2022"""
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from urllib.request import urlopen, Request
import json 

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


"""
The get_sentiment() function returns a number between -1 and 1 for a given string (sentence).  
The higher the number, the more positive the sentiment is.  
"""
def get_sentiment(sentence):     
    return sid.polarity_scores(sentence)['compound']

#Exercise1

def get_sentimentlist(my_list):
    """This function receives a list of strings as input and returns a list of corresponding sentiments."""
    n = []
    for sentence in my_list:
        a = get_sentiment(sentence)
        n.append(a)
    return n
my_list = ['good day!','terrible day','I love today','I feel sad']


#Exercise2

def get_max_score(my_list):
    """This function receives a list of strings as input returns the maximum score."""
    n2 = get_sentimentlist(my_list)
    n2.sort()
    maxitem = n2.pop()
    return maxitem

#Exercise3

def get_min_score(my_list):
    """This function receives a list of strings as input returns the minimum score."""
    n2 = get_sentimentlist(my_list)
    n2.sort()
    minitem = n2.pop(0)
    return minitem

#Exercise4

def positive_only(my_list):
    """This function receives a list of strings as input return only the positive strings."""
    n3 = []
    for sentence in my_list:
        a = get_sentiment(sentence)
        if a > 0:
            n3.append(sentence)
    return n3

#Exercise5

def negative_only(my_list):
    """This function receives a list of strings as input return only the negative strings."""
    n3 = []
    for sentence in my_list:
        a = get_sentiment(sentence)
        if a < 0:
            n3.append(sentence)
    return n3

"""
The get_reddit_news function return a list of current world news titles from reddit's worldnews 
"""
def get_reddit_news(url = 'https://www.reddit.com/r/worldnews/.json'):
    """ Retrieve the contents of a web page.
    """
    my_socket = urlopen(Request(url, headers={'User-Agent':'abcde'}))
    dta = my_socket.read()
    reddit_data = json.loads(dta)    
    titles = [x['data']['title'] for x in reddit_data['data']['children']]
    return titles


#Exercise6
def get_most_positive_news():
    """This function receives a list of current reddit news as input return only the most positive news."""
    news_list = get_reddit_news(url = 'https://www.reddit.com/r/worldnews/.json')
    news_positive_list = positive_only(news_list)
    news_positive_list.sort()
    return news_positive_list.pop()

#Exercise7
def get_most_negative_news():
    """This function receives a list of current reddit news as input return only the most negative news."""
    news_list = get_reddit_news(url = 'https://www.reddit.com/r/worldnews/.json')
    news_negative_list = negative_only(news_list)
    news_negative_list.sort()
    return news_negative_list.pop(0)

def main():
    print(get_most_negative_news())
    print(get_most_positive_news())      
if __name__ == "__main__":
    main()


