import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment_scores(text, threshold = 0.05):
  analyzer = SentimentIntensityAnalyzer()
  scores = analyzer.polarity_scores(text)

  compound_score = scores['compound']

  if compound_score >= threshold:
      return "Positive"
  elif compound_score <= -threshold:
      return "Negative"
  else:
      return "Neutral"