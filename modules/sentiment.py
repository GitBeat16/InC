from newsapi import NewsApiClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

newsapi = NewsApiClient(api_key="YOUR_NEWS_API_KEY")

def get_news_sentiment(ticker):
    articles = newsapi.get_everything(q=ticker, language='en', sort_by='publishedAt', page_size=10)
    
    sid = SentimentIntensityAnalyzer()
    scores = []

    for article in articles['articles']:
        headline = article['title']
        score = sid.polarity_scores(headline)['compound']
        scores.append(score)

    avg_score = sum(scores) / len(scores) if scores else 0

    return avg_score, articles['articles']
