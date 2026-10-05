import nltk
from nltk.corpus import gutenberg

nltk.download("gutenberg")
print(gutenberg.fileids())
moby_dick_text = gutenberg.words('melville-moby_dick.txt')
print("First 100 words from 'Moby-Dick':")
print(moby_dick_text[:100])
