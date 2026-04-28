from transformers import pipeline
import textwrap
print("Loading model... ")
summarizer = pipeline("summarization",model="sshleifer/distilbart-cnn-12-6")
print("✅ Model loaded successfully!\n")
input_text = """
Artificial Intelligence (AI) is a rapidly evolving field of computer science that aims to create systems 
capable of performing tasks that typically require human intelligence. These tasks include problem-solving, 
learning, reasoning, perception, and language understanding.AI technologies have seen significant growth due to advances in machine learning, deep learning, and the 
availability of large datasets. In recent years, AI has been applied across various domains such as healthcare, 
finance, transportation, and education.In healthcare, AI helps diagnose diseases and recommend treatments. In finance, it is used for fraud detection 
and trading. Autonomous vehicles are transforming transportation, while personalized learning is improving education.
Despite its benefits, AI raises ethical concerns such as job displacement, bias, and data privacy issues.
"""
print("📄 ORIGINAL TEXT:\n")
print(textwrap.fill(input_text, width=100))
summary = summarizer(input_text,max_length=120,min_length=40,do_sample=False)
print("\n📝 GENERATED SUMMARY:\n")
print(textwrap.fill(summary[0]['summary_text'], width=100))
