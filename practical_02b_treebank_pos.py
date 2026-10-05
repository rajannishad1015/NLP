import nltk
from nltk.corpus import treebank_chunk

nltk.download("treebank")
nltk.download("averaged_perceptron_tagger_eng")

doc = treebank_chunk.tagged_sents()[0]
print(doc)

nouns = []
for word, tag in doc:
    if tag in ["NN", "NNS", "NNP", "NNPS"]:
        nouns.append(word)
print("Nouns Found:", nouns)
