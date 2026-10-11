
import streamlit as st
from chatbot import FAQChatbot

st.set_page_config(
    page_title="Smart FAQ Chatbot",
    page_icon="💬",
    layout="centered"
)

# Initialize chatbot
@st.cache_resource
def load_chatbot():
    return FAQChatbot("faqs.csv")

bot = load_chatbot()

# Page heading
st.title("💬 Smart FAQ Chatbot")
st.write(
    "Ask questions about college admissions, courses, "
    "fees, scholarships and examinations."
)

st.caption("Powered by NLP, TF-IDF-style weighting and cosine similarity.")

# Store conversation in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("About the Chatbot")
    st.write(
        "This chatbot compares your question with a FAQ dataset "
        "and returns the closest matching answer."
    )

    st.subheader("Try asking")
    examples = [
        "How do I apply for admission?",
        "Are scholarships available?",
        "What are the college fees?",
        "How do I get my exam timetable?"
    ]

    for question in examples:
        if st.button(question, use_container_width=True):
            st.session_state.pending_question = question

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant" and "score" in message:
            st.caption(
                f"Category: {message['category']} | "
                f"Similarity: {message['score']:.2f}"
            )

# Accept typed or suggested question
pending = st.session_state.pop("pending_question", None)
user_question = st.chat_input("Type your question...")

question = user_question or pending

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    result = bot.get_answer(question)

    with st.chat_message("assistant"):
        st.markdown(result["answer"])
        st.caption(
            f"Category: {result['category']} | "
            f"Similarity: {result['score']:.2f}"
        )

    st.session_state.messages.append({
        "role": "assistant",
        "content": result["answer"],
        "category": result["category"],
        "score": result["score"]
    })