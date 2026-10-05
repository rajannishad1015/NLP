from sklearn.feature_extraction.text import TfidfVectorizer

t1 = input("Enter term 1: ")
t2 = input("Enter term 2: ")
t3 = input("Enter term 3: ")

document = (t1, t2, t3)
my_terms = ["india", "technology", "economy"]
tfidf = TfidfVectorizer(vocabulary=my_terms)
result = tfidf.fit_transform(document)
print("\nIDF Values:")

features_names = tfidf.get_feature_names_out()
idf_values = tfidf.idf_

for i in range(len(features_names)):
    print(features_names[i], ':', idf_values[i])
print("\nWords Index")
print(tfidf.vocabulary_)

print("TF-IDF Matrix (Sparse Formate)")
print(result)

print("\nTF-IDF matrix(Array Format):")
print(round(result, 2).toarray())
