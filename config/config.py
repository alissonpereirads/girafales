import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")


def get_groq():
    return ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key)
