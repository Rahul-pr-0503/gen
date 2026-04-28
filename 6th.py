from transformers import pipeline
from typing import List, Dict
class SentimentAnalyzer:
    """
    A class to handle sentiment analysis using Hugging Face pipeline
    """
    def __init__(self, model_name: str = None):
        """
        Initialize the sentiment analysis pipeline
        :param model_name: Optional custom model
        """
        try:
            if model_name:
                self.analyzer = pipeline("sentiment-analysis", model=model_name)
            else:
                self.analyzer = pipeline("sentiment-analysis")
            print("[INFO] Sentiment model loaded successfully.")
        except Exception as e:
            print("[ERROR] Failed to load model:", e)
            raise
    def analyze(self, texts: List[str]) -> List[Dict]:
        """
        Perform sentiment analysis
        :param texts: List of input sentences
        :return: List of sentiment results
        """
        try:
            results = self.analyzer(texts)
            return results
        except Exception as e:
            print("[ERROR] Analysis failed:", e)
            return []
    def display_results(self, texts: List[str], results: List[Dict]) -> None:
        """
        Display formatted output 
        :param texts: Input sentences
        :param results: Model predictions
        """
        print("\n========== SENTIMENT ANALYSIS RESULTS ==========\n")
        for idx, (text, result) in enumerate(zip(texts, results), start=1):
            print(f"[{idx}] Sentence       : {text}")
            print(f"    Sentiment      : {result['label']}")
            print(f"    Confidence     : {result['score']:.4f}")
            print("-" * 60)
def load_sample_data() -> List[str]:
    """
    Load sample sentences (simulating real-world input)
    """
    return [
        "I absolutely love this product!",
        "This is the worst experience ever.",
        "The service was okay, nothing special.",
        "Very fast delivery and great support.",
        "I am unhappy with the performance."
    ]
def main():
    """
    Main execution function
    """
    print("\n[INFO] Starting Sentiment Analysis Application...\n")
    analyzer = SentimentAnalyzer()
    sentences = load_sample_data()
    results = analyzer.analyze(sentences)
    analyzer.display_results(sentences, results)
if __name__ == "__main__":
    main()
