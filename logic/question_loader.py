# logic/question_loader.py

import json
import random
from cohere_ai.question_generator import generate_question
from cohere_ai.difficulty_classifier import classify_difficulty

def load_static_questions(file_path: str, count: int = 5) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        all_questions = json.load(f)
    return random.sample(all_questions, min(count, len(all_questions)))

def load_ai_questions(subject: str, topic: str, count: int = 5) -> list:
    questions = []
    for _ in range(count):
        generated = generate_question(subject=subject, topic=topic)
        if "question" in generated and "options" in generated and "answer" in generated:
            if "difficulty" not in generated:
                generated["difficulty"] = classify_difficulty(generated["question"])
            questions.append(generated)
    return questions

def load_mixed_questions(static_path: str, subject: str, topic: str, static_count=5, ai_count=5) -> list:
    static_qs = load_static_questions(static_path, static_count)
    ai_qs = load_ai_questions(subject, topic, ai_count)
    all_qs = static_qs + ai_qs
    random.shuffle(all_qs)
    return all_qs
