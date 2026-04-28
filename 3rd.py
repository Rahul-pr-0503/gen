from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
medical_corpus = [
    "The doctor prescribed antibiotics for the infection",
    "The patient was diagnosed with diabetes and hypertension",
    "Surgery was performed to remove the tumor",
    "The nurse monitored the patient's vital signs",
    "Cardiology deals with heart related diseases",
    "Neurology focuses on brain and nervous system disorders",
    "The hospital provides emergency medical services",
    "Cancer treatment includes chemotherapy and radiation therapy",
    "The pharmacist dispensed the prescribed medication",
    "The diagnosis was confirmed after laboratory tests"
]
processed_corpus = [simple_preprocess(sentence) for sentence in medical_corpus]
print("Processed Corpus:\n")
for sentence in processed_corpus:
    print(sentence)
model = Word2Vec(
    sentences=processed_corpus,
    vector_size=100,   
    window=5,
    min_count=1,
    workers=4
)
print("\nWord2Vec Model Trained Successfully!\n")
def get_similar_words(word):
    print(f"\nTop 5 similar words for '{word}':\n")
    similar_words = model.wv.most_similar(word, topn=5)
    for w, score in similar_words:
        print(f"{w}  (Score: {score:.4f})")
get_similar_words("doctor")
print("\nSimilarity Scores:\n")
print("doctor & nurse:",
      round(model.wv.similarity("doctor", "nurse"), 4))
print("cancer & tumor:",
      round(model.wv.similarity("cancer", "tumor"), 4))
print("brain & heart:",
      round(model.wv.similarity("brain", "heart"), 4))
def generate_context(word):
    similar = [w for w, _ in model.wv.most_similar(word, topn=3)]
    sentence = f"In medical context, {word} is closely associated with {', '.join(similar)}."
    return sentence
print("\nContextual Output:")
print(generate_context("cancer"))
