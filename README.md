# CodeAlpha Task 2: Smart FAQ Chatbot

## About
A college FAQ chatbot that uses text preprocessing, TF-IDF-style word weighting, and cosine similarity to find the closest matching FAQ answer. It includes a Streamlit chat interface, conversation history, category labels, similarity scores, and a fallback response for unmatched questions.

## Features
- Natural-language question matching
- FAQ dataset stored in CSV format
- Cosine similarity matching
- Confidence-threshold fallback
- Interactive Streamlit interface
- Chat history and suggested questions

## Technologies
- Python
- Streamlit
- Python standard library (CSV, regular expressions, math, collections)

## Project Files
- `app.py` — Streamlit user interface
- `chatbot.py` — text processing and similarity matching
- `faqs.csv` — FAQ dataset
- `test_chatbot.py` — basic test questions
- `requirements.txt` — dependency list

## Setup
1. Install Python 3.12 or a compatible Python version.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment if needed.
4. Install dependencies: `python -m pip install -r requirements.txt`
5. Start the app: `python -m streamlit run app.py`
6. Open the local URL shown in the terminal.

## Note
This project uses a lightweight TF-IDF-style weighting and cosine similarity implementation written in Python; it does not use a trained machine-learning model. FAQ answers should be checked against the relevant institution's official information before use.