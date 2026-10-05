from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

sentences = [
    ["rahul", "goes", "to", "college"],
    ["neha", "studies", "data", "science"],
    ["priya", "travels", "by", "train"],
    ["students", "learn", "machine", "learning"],
    ["college", "learns", "artificial", "intelligence"],
]

model = Word2Vec(sentences, vector_size=50, window=2, min_count=1, sg=0)
words = list(model.wv.index_to_key)
print(words)
vectors = [model.wv[word] for word in words]
print(vectors)
pca = PCA(n_components=2)
pca_result = pca.fit_transform(vectors)
plt.figure()
plt.scatter(pca_result[:, 0], pca_result[:, 1])
for i, word in enumerate(words):
    plt.annotate(word, xy=(pca_result[i, 0], pca_result[i, 1]))

plt.title("Word2Vec Word Embeddings Visualized with PCA")
plt.show()
