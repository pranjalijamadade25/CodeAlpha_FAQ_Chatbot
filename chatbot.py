
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FAQChatbot:
    def __init__(self, csv_path="faqs.csv"):
        # Load FAQ questions and answers
        self.faqs = pd.read_csv(csv_path)

        self.questions = self.faqs["question"].fillna("").tolist()

        # Convert questions into numerical vectors
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )

        self.question_vectors = self.vectorizer.fit_transform(
            self.questions
        )

    def get_answer(self, user_question):
        user_question = user_question.strip()

        if not user_question:
            return {
                "answer": "Please enter a question.",
                "score": 0.0,
                "category": "General"
            }

        # Convert user question into a TF-IDF vector
        user_vector = self.vectorizer.transform([user_question])

        # Compare it with all stored FAQ questions
        scores = cosine_similarity(
            user_vector,
            self.question_vectors
        )[0]

        # Find the most similar FAQ
        best_index = scores.argmax()
        best_score = float(scores[best_index])

        # Reject unrelated questions
        threshold = 0.20

        if best_score < threshold:
            return {
                "answer": (
                    "Sorry, I couldn't find a suitable answer. "
                    "Please try asking in a different way."
                ),
                "score": best_score,
                "category": "Unmatched"
            }

        best_faq = self.faqs.iloc[best_index]

        return {
            "answer": str(best_faq["answer"]),
            "score": best_score,
            "category": str(best_faq["category"])
        }