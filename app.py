# app.py

import streamlit as st
import random
import json
from logic.adaptive_engine import get_next_difficulty, calculate_score
from cohere_ai.answer_explainer import explain_answer
from logic.question_loader import load_mixed_questions

# App config
st.set_page_config(page_title="Adaptive Science Quiz", layout="centered")
st.title("🧪 Adaptive Science Quiz (AI-powered)")
st.caption("Built with ❤️ by Armaan Sharma")

# Session state setup
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.difficulty = "easy"
    st.session_state.quiz_done = False
    st.session_state.answered = False
    st.session_state.explanation = ""

# Load and shuffle questions once
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = load_mixed_questions(
        static_path="questions/science_questions_difficulty_tagged.json",
        subject="science",
        topic="physics",
        static_count=5,
        ai_count=5
    )

# Get current question
question_data = st.session_state.shuffled_questions[st.session_state.question_index]

# Show question
st.subheader(f"Q{st.session_state.question_index + 1}: {question_data['question']}")

# Show options
selected = st.radio(
    "Choose an option:",
    list(question_data["options"].items()),
    format_func=lambda x: f"{x[0]}) {x[1]}",
    key=f"radio_{st.session_state.question_index}"
)

# Submit button logic
if not st.session_state.answered:
    if st.button("Submit Answer"):
        user_answer = selected[0]
        correct_answer = question_data["answer"]
        is_correct = user_answer == correct_answer

        # Feedback
        if is_correct:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. Correct answer: {correct_answer}) {question_data['options'][correct_answer]}")

        # Score + difficulty update
        st.session_state.score = calculate_score(
            st.session_state.score,
            is_correct,
            question_data["difficulty"]
        )
        st.session_state.difficulty = get_next_difficulty(
            st.session_state.difficulty,
            is_correct
        )

        st.session_state.answered = True

# Explanation button (only visible after answering)
if st.session_state.answered and not st.session_state.explanation:
    if st.button("Why is this the correct answer?"):
        with st.spinner("Generating explanation..."):
            explanation = explain_answer(
                question=question_data["question"],
                correct_option=question_data["answer"],
                correct_answer=question_data["options"][question_data["answer"]]
            )
            st.session_state.explanation = explanation

# Show explanation if available
if st.session_state.explanation:
    st.info(st.session_state.explanation)

# Next Question button
if st.session_state.answered:
    if st.button("Next Question"):
        st.session_state.question_index += 1
        st.session_state.answered = False
        st.session_state.explanation = ""

        if st.session_state.question_index >= len(st.session_state.shuffled_questions):
            st.session_state.quiz_done = True
        st.rerun()

# Quiz completed
if st.session_state.quiz_done:
    st.markdown("---")
    st.success(f"🎉 Quiz Completed! Your final score: **{st.session_state.score} / 15**")

    if st.button("Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
