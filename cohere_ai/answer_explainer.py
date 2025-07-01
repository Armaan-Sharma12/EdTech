# cohere_ai/answer_explainer.py

from cohere_ai.cohere_client import generate_completion

def explain_answer(question: str, correct_option: str, correct_answer: str) -> str:
    """
    Uses Cohere to generate an explanation for the correct answer to a question.
    """
    prompt = f"""
Explain the correct answer for the following multiple-choice question in a way a high school student would understand:

Question: {question}
Correct Option: {correct_option}
Answer: {correct_answer}

Provide a simple explanation:
"""

    explanation = generate_completion(prompt, temperature=0.6, max_tokens=150)
    
    if not explanation:
        return "Sorry, an explanation couldn't be generated."

    return explanation.strip()
