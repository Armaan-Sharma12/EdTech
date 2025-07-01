#  EdTech AI Assessment Engine

This project is an **AI-powered adaptive learning platform** designed to enhance education through intelligent question analysis and generation. It uses the **Cohere API** to classify difficulty levels, generate new questions, and explain answers, forming a robust backend for EdTech applications.

---

##  Features

-  **Difficulty Classification** of questions using Cohere embeddings
-  **Question Generation** for dynamic quizzes
-  **Answer Explanation** to support student learning
-  **Adaptive Engine** for personalized question delivery
-  JSON-based question datasets for Science subjects

---

##  Project Structure

edtech-project/  
│   
├── cohere_ai/ # All Cohere-based AI modules   
│ ├── answer_explainer.py   
│ ├── cohere_client.py   
│ ├── difficulty_classifier.py   
│ └── question_generator.py   
│   
├── logic/ # Core logic for adaptivity and loading   
│ ├── adaptive_engine.py   
│ └── question_loader.py    
│   
├── questions/ # Datasets used for testing and training   
│ ├── science_questions_cleaned.json   
│ └── science_questions_difficulty_tagged.json   
│   
├── app.py # Entry point for testing or frontend integration   
├── .env # Stores COHERE_API_KEY   
├── .gitignore # Ignores venv and env files   
└── requirements.txt # Python dependencies   


---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/edtech-ai-engine.git
cd edtech-ai-engine
```

### 2. Setup Environment

```bash
python -m venv .venv
.venv\Scripts\activate     # On Windows
pip install -r requirements.txt
```

### 3. Add your Cohere API Key

Create a ```.env``` file in the root directory:

```bash
COHERE_API_KEY=your_actual_key_here
```

Get your key from Cohere Dashboard.

### 4. Run the App

```bash
python app.py
```

This will test the full pipeline (load questions, classify difficulty, and explain answers).

---

## Example Use Cases

1. ```difficulty_classifier.py``` → Classifies how hard a question is
2. ```question_generator.py``` → Generates new science-based questions
3. ```answer_explainer.py``` → Generates a simplified explanation of the correct answer
4. ```adaptive_engine.py``` → Selects the next best question based on student progress

## Dependencies

1. ```cohere```
2. ```python-dotenv```
3. ```pandas```
4. ```json```
5. ```os```

Install via:

```bash
pip install -r requirements.txt
```

## Notes

1. All Cohere logic is modularized in ```cohere_ai/``` for reusability.
2. Dataset uses cleaned and tagged science questions.
3. Ready for integration with Streamlit, Flask, or any frontend.

##  Author

Built by Armaan Sharma
Intern @ Marksman | 2025

## Connect With Me

linkedIn - ```https://www.linkedin.com/in/armaan-sharma-0885b9309/```
Mail - ```armaan.sharma2003@gmail.com```
Follow Me in Github

---

Let me know if you'd like me to include badges (like Python version, license, etc.), or instructions for Streamlit frontend integration.


