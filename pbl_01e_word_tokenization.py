import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt_tab")
text = input("enter the text: ")
tokens = word_tokenize(text)
print("word tokens:", tokens)
