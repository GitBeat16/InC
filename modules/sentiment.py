import os
from newsapi import NewsApiClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download once
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except:
    nltk.download('vader_lexicon')

newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

def get_news_sentiment(ticker):
    try:
        data = newsapi.get_everything(
            q=ticker,
            language='en',
            sort_by='publishedAt',
            page_size=10
        )

        articles = data.get("articles", [])

        sid = SentimentIntensityAnalyzer()
        scores = []
        headlines = []

        for article in articles:
            title = article.get("title")
            if title:
                score = sid.polarity_scores(title)['compound']
                scores.append(score)
                headlines.append(title)

        # Weighted sentiment
        weighted_score = 0
        total_weight = 0

        for i, score in enumerate(scores):
            weight = i + 1
            weighted_score += score * weight
            total_weight += weight

        avg_score = weighted_score / total_weight if total_weight else 0

        return avg_score, headlines

    except Exception as e:
        return 0, []
