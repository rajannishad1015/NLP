from textblob import TextBlob

sentence1 = input("Enter the sentence: ")
sentence2 = input("Enter the sentence: ")
sentence3 = input("Enter the sentence: ")

sentences = [sentence1, sentence2, sentence3]
for sentence in sentences:
    blob = TextBlob(sentence)
    print(sentence)
    print("Sentiment score:", round(blob.sentiment.polarity, 2))
    print()
