import gensim.downloader as api
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
print("Loading pre-trained word vectors...")
model = api.load("glove-wiki-gigaword-100")
print("Model loaded!")
print("Vector size:", model.vector_size)
def word_similarity(word1, word2):
    sim = model.similarity(word1, word2)
    print(f"Similarity between '{word1}' and '{word2}': {sim:.4f}")
def word_analogy(positive, negative, topn=5):
    print(f"\nAnalogy: {positive} - {negative}")
    results = model.most_similar(
        positive=positive,
        negative=negative,
        topn=topn
    )
    for word, score in results:
        print(f"{word:10s} {score:.4f}")
print("\n--- Word Similarities ---")
word_similarity("king", "queen")
word_similarity("king", "car")
word_similarity("paris", "france")
print("\n--- Vector Arithmetic Examples ---")
word_analogy(positive=["king", "woman"], negative=["man"])
word_analogy(positive=["france", "rome"], negative=["paris"])
word_analogy(positive=["walking", "swim"], negative=["walk"])
print("\n--- Bias Demonstration (for analysis) ---")
word_analogy(positive=["doctor", "woman"], negative=["man"])
print("\nVisualizing word relationships...")
words = [
    "king", "queen", "man", "woman",
    "prince", "princess", "france", "paris",
    "italy", "rome"
]
vectors = np.array([model[word] for word in words])
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(vectors)
plt.figure(figsize=(8, 6))
for word, (x, y) in zip(words, reduced_vectors):
    plt.scatter(x, y)
    plt.text(x + 0.01, y + 0.01, word)
plt.title("Word Vector Relationships (PCA Projection)")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.grid(True)
plt.show()
