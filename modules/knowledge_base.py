import json
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


SYNONYMS = {
    "money": "refund",
    "returned": "refund",
    "return": "refund",
    "returning": "refund",
    "cash": "refund",
    "package": "order",
    "parcel": "order",
    "shipping": "delivery",
    "ship": "delivery",
    "arrive": "delivery",
    "arrived": "delivery"
}


def normalize_text(text):
    text = text.lower()

    for word, replacement in SYNONYMS.items():
        text = re.sub(
            rf"\b{word}\b",
            replacement,
            text
        )

    return text


def load_faq():
    with open("data/faq.json", "r", encoding="utf-8") as file:
        return json.load(file)


def find_answer(user_question, faq_data):

    user_question = normalize_text(user_question)

    questions = [
        normalize_text(item["question"])
        for item in faq_data
    ]

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(
        questions + [user_question]
    )

    similarities = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    ).flatten()

    best_index = similarities.argmax()
    best_score = similarities[best_index]

    if best_score < 0.15:
        return None, best_score

    return faq_data[best_index], best_score