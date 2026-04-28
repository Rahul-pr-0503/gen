import nltk
from gensim.models import Word2Vec
from nltk.corpus import brown
nltk.download('brown')
sentences = brown.sents()
processed_sentences = [[word.lower() for word in sent] for sent in sentences]
model = Word2Vec(
    processed_sentences,
    vector_size=100,
    window=5,
    min_count=2,
    workers=4
)
seed_word = input("Enter a word: ").lower()
try:
    similar_words = model.wv.most_similar(seed_word, topn=5)
    similar_words = [word for word, score in similar_words]
except KeyError:
    print("❌ Word not found in vocabulary. Try another word.")
    exit()
print("\n✅ Similar Words:", similar_words)
def generate_paragraph(seed, words):
    paragraph = (
        f"\nOnce upon a time, there was a {seed} who lived in a distant land. "
        f"One day, it met a {words[0]} and a {words[1]} who became its companions. "
        f"Together, they explored places that were {words[2]} and magical. "
        f"They faced many challenges but stayed {words[3]} and brave. "
        f"In the end, the {seed} realized that being {words[4]} is the key to happiness."
    )
    return paragraph

story = generate_paragraph(seed_word, similar_words)
print("\n📝 Generated Paragraph:")
print(story)