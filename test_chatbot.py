
from chatbot import FAQChatbot

bot = FAQChatbot()

questions = [
    "How do I take admission?",
    "Tell me about scholarships",
    "Where can I find my exam timetable?",
    "What is the weather today?"
]

for question in questions:
    result = bot.get_answer(question)

    print("\nQuestion:", question)
    print("Answer:", result["answer"])
    print("Category:", result["category"])
    print("Similarity:", round(result["score"], 3))