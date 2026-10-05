from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.decomposition import NMF

documents = input("Enter sentence on one topic only: ").split(".")
vectorizer = CountVectorizer(stop_words='english')
x = vectorizer.fit_transform(documents)

lds = LatentDirichletAllocation(n_components=2)
lds.fit(x)

nmf = NMF(n_components=2)
nmf.fit(x)

words = vectorizer.get_feature_names_out()
print("Topic modelling using LDA")
topic_number = 1
for topic in lds.components_:
    print("Topic", topic_number)
    top_words = topic.argsort()[-2:]
    for index in top_words:
        print(words[index])
    topic_number += 1
    print()

print("Topic modelling using nmf")
topic_number = 1
for topic in nmf.components_:
    print("Topic", topic_number)
    top_words = topic.argsort()[-2:]
    for index in top_words:
        print(words[index])
    topic_number += 1
