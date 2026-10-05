import math

corpus = [
    "india is growing fast in the technology sector",
    "the technology industry in india is creating new opportunities",
    "agriculture remain to backborn of indian economy"
]
term = "technology"
N = len(corpus)
df = 0
for doc in corpus:
    words = doc.split()
    if term in words:
        df = df + 1
    print("Document Frequency=", df)

idf = math.log10(N / df)
print("IDF=", round(idf, 3))

for i, doc in enumerate(corpus):
    words = doc.split()
    tf = words.count(term) / len(words)
    tfidf = tf * idf
    print(f"Document{i+1}")
    print("TF=", round(tf, 3))
    print("TF-IDF=", round(tfidf, 3))
