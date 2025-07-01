# cohere_ai/question_generator.py

from cohere_ai.cohere_client import generate_completion

def generate_question(subject: str, topic: str, difficulty: str = "easy") -> dict:
    prompt = f"""
Generate a {difficulty}-level multiple choice question for high school {subject} on the topic of {topic}.
Include exactly five options (A, B, C, D, E) and clearly indicate the correct answer.
Respond in the following format:
Question: <text>
Options:
A. ...
B. ...
C. ...
D. ...
E. ...
Answer: <correct option letter>
"""
    raw_text = generate_completion(prompt)
    
    if not raw_text:
        return {"error": "Generation failed"}

    # Naive parsing
    lines = raw_text.strip().split('\n')
    question_data = {"question": "", "options": {}, "answer": ""}

    for line in lines:
        if line.startswith("Question:"):
            question_data["question"] = line.replace("Question:", "").strip()
        elif line.startswith("A."):
            question_data["options"]["A"] = line[3:].strip()
        elif line.startswith("B."):
            question_data["options"]["B"] = line[3:].strip()
        elif line.startswith("C."):
            question_data["options"]["C"] = line[3:].strip()
        elif line.startswith("D."):
            question_data["options"]["D"] = line[3:].strip()
        elif line.startswith("E."):
            question_data["options"]["E"] = line[3:].strip()
        elif line.startswith("Answer:"):
            question_data["answer"] = line.replace("Answer:", "").strip()

    return question_data
