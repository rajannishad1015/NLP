import nltk
from nltk.corpus import brown

nltk.download("brown")
print(brown.categories())

news_word = brown.words(categories='news')
print("first 20 word from the goverment categories:", news_word[0:20])
