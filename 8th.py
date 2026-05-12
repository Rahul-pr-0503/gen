import cohere
co = cohere.Client("B9LOgKHu6ji6OWsy8OCLLCEem7KldDXgv9i82yOA")
input_text = "How to construct good College"
prompt = f"""
Analyze the text and give:
1. Title
2. Summary
3. Key Points
4. Conclusion
Text:
{input_text}
"""
response = co.chat(
    message=prompt,
    model="command-r-08-2024",
    temperature=0.7
)
print(response.text)
