from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
from transformers import pipeline
ai_corpus = [
    "Artificial intelligence improves automation",
    "Machine learning algorithms learn from data",
    "Deep learning uses neural networks",
    "Natural language processing enables chatbots",
    "AI helps in robotics and autonomous systems",
    "Data science uses statistics and machine learning",
    "Neural networks power modern AI applications",
    "AI models generate text images and speech",
    "Chatbots use natural language understanding",
    "Automation increases productivity using AI"
]
processed_corpus = [simple_preprocess(sentence) for sentence in ai_corpus]
print("Processed Corpus:\n")
for s in processed_corpus:
    print(s)
model = Word2Vec(
    sentences=processed_corpus,
    vector_size=100,
    window=5,
    min_count=1,
    workers=4
)
print("\nWord2Vec Model Trained Successfully!\n")
word = "ai"
similar_words = model.wv.most_similar(word, topn=3)
print("Similar words for 'ai':\n")
for w, score in similar_words:
    print(w, ":", round(score,4))
original_prompt = "Explain the benefits of AI in healthcare."
similar_list = [w for w,_ in similar_words]
enriched_prompt = f"Explain the benefits of AI, {similar_list[0]}, {similar_list[1]}, and {similar_list[2]} in healthcare."
print("\nOriginal Prompt:")
print(original_prompt)
print("\nEnriched Prompt:")
print(enriched_prompt)
generator = pipeline("text-generation", model="gpt2")
original_output = generator(original_prompt, max_length=60, num_return_sequences=1)
enriched_output = generator(enriched_prompt, max_length=60, num_return_sequences=1)
print("\nResponse for Original Prompt:\n")
print(original_output[0]['generated_text'])
print("\nResponse for Enriched Prompt:\n")
print(enriched_output[0]['generated_text'])
