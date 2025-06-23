from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text):
        score = self.analyzer.polarity_scores(text)['compound']
        label = (
            "positive" if score > 0.2 else
            "negative" if score < -0.2 else
            "neutral"
        )
        return {"score": score, "label": label}
