import nltk
from nltk import word_tokenize, bigrams
from collections import Counter

nltk.download("punkt")

text = input("Enter training sentences: ")
words = word_tokenize(text.lower())
unigram_counts = Counter(words)
bigram_counts = Counter(bigrams(words))
sentence = input("Enter the sentence from training Sentences: ")
input_words = word_tokenize(sentence.lower())
input_bigrams = list(bigrams(input_words))
probability = 1
for w1, w2 in input_bigrams:
    if unigram_counts[w1] > 0:
        probability *= bigram_counts[(w1, w2)] / unigram_counts[w1]
    else:
        probability = 0
print("Bigrams:", input_bigrams)
print("Probability:", probability)
