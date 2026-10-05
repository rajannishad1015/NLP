from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

documents = input("Enter a Sentence on one topic only: ").split(".")
vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(documents)
lds = LatentDirichletAllocation(n_components=2)
lds.fit(X)

words = vectorizer.get_feature_names_out()
topic_number = 1
for topic in lds.components_:
    print("Topic", topic_number)
    top_words = topic.argsort()[-2:]
    for index in top_words:
        print(words[index])
    topic_number += 1
    print()
