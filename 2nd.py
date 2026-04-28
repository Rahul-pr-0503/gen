import gensim.downloader as api
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
print("Loading GloVe Model (100D)... Please wait.")
model = api.load("glove-wiki-gigaword-100")
print("Model Loaded Successfully!\n")
tech_words = [
    "computer", "software", "hardware", "internet", "network",
    "database", "algorithm", "python", "cloud", "security"
]
word_vectors = []
valid_words = []
for word in tech_words:
    if word in model:
        word_vectors.append(model[word])
        valid_words.append(word)
word_vectors = np.array(word_vectors)
print("Words used for visualization:")
print(valid_words)
print("\nTotal words:", len(valid_words))
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(word_vectors)
print("\nDimensionality Reduction Completed!")
print("Reduced shape:", reduced_vectors.shape)
plt.figure()
plt.scatter(reduced_vectors[:, 0], reduced_vectors[:, 1])
for i, word in enumerate(valid_words):
    plt.annotate(word, (reduced_vectors[i, 0], reduced_vectors[i, 1]))
plt.title("PCA Visualization of Technology Word Embeddings")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()
print("\n--- Similarity Analysis ---\n")
print("Similarity between computer & software:",
      round(model.similarity("computer", "software"), 4))
print("Similarity between internet & network:",
      round(model.similarity("internet", "network"), 4))
print("Similarity between python & algorithm:",
      round(model.similarity("python", "algorithm"), 4))
def get_similar_words(word):
    if word in model:
        print(f"\nTop 5 similar words for '{word}':\n")
        similar = model.most_similar(word, topn=5)
        for w, score in similar:
            print(f"{w}  (Score: {score:.4f})")
    else:
        print("Word not found in vocabulary.")
get_similar_words("computer")
def generate_context(word):
    if word in model:
        similar_words = [w for w, _ in model.most_similar(word, topn=5)]
        sentence = f"{word.capitalize()} is strongly related to " + ", ".join(similar_words) + \
                   ", showing semantic connections in the technology domain."
        return sentence
    else:
        return "Word not found in vocabulary."
print("\nContextual Output:")
print(generate_context("cloud"))
