# cohere_ai/difficulty_classifier.py

from cohere_ai.cohere_client import generate_completion

def classify_difficulty(question_text: str) -> str:
    """
    Classifies the difficulty of a multiple-choice question as 'easy', 'medium', or 'hard'
    using Cohere's language understanding.
    """
    prompt = f"""
Classify the following multiple-choice question as easy, medium, or hard for high school students:

Question: {question_text}

Respond with only one word: easy, medium, or hard.
"""
    label = generate_completion(prompt, temperature=0.3, max_tokens=10)

    if not label:
        return "medium"  # Fallback if no response

    label = label.lower().strip()

    if label in ["easy", "medium", "hard"]:
        return label
    else:
        return "medium"  # Fallback for unexpected responses
