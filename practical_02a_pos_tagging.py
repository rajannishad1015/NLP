import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt_tab')

sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

nouns = []
for word, tag in tagged:
    if tag in ["NN", "NNS", "NNP", "NNPS"]:
        nouns.append(word)
print("Nouns Found:", nouns)
