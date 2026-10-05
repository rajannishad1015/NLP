from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

sentences = input("Enter sentences having sentiments: ").split(".")

for sentence in sentences:
    score = analyzer.polarity_scores(sentence)
    print(sentence)
    print(round(score['compound'], 2))
    print()
