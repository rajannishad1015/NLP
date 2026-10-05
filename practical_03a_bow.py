from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "This is the first document.",
    "This document is the second doucement.",
    "And this is the third doucment.",
    "is This the first document?"
]

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corpus)
print("vocabulary()bow:", vectorizer.get_feature_names_out())
print("bow matrix:\n", x.toarray())

print("vocabulary()bow:", vectorizer.get_feature_names_out())
print("bow matrix:\n", x.toarray())
