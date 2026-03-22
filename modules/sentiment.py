import os
from newsapi import NewsApiClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except:
    nltk.download('vader_lexicon')

newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

def get_news_sentiment(ticker):
    try:
        articles = newsapi.get_everything(q=ticker, language='en', page_size=10)
        sid = SentimentIntensityAnalyzer()

        scores = []
        headlines = []

        for article in articles['articles']:
            title = article.get("title")
            if title:
                score = sid.polarity_scores(title)['compound']
                scores.append(score)
                headlines.append(title)

        avg_score = sum(scores)/len(scores) if scores else 0
        return avg_score, headlines

    except:
        return 0, []