import nltk
from nltk import word_tokenize, bigrams, trigrams
from collections import Counter

nltk.download("punkt")
text = input("Enter training sentences: ")
words = word_tokenize(text.lower())
bigram_counts = Counter(bigrams(words))
trigram_counts = Counter(trigrams(words))
sentence = input("Enter the sentence from training Sentences: ")
input_words = word_tokenize(sentence.lower())
input_trigrams = list(trigrams(input_words))
probability = 1
for w1, w2, w3 in input_trigrams:
    if bigram_counts[(w1, w2)] > 0:
        probability *= trigram_counts[(w1, w2)] / bigram_counts[(w1, w2)]
    else:
        probability = 0
print("trigrams:", input_trigrams)
print("Probability:", probability)
