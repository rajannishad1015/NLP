import nltk
from nltk.corpus import reuters

nltk.download('reuters')
print(reuters.fileids())
reuters_text = reuters.words('test/15217')
print("first 100 word of reuters document:", reuters_text[1:100])
