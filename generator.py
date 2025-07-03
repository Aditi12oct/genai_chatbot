import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load your .env with GEMINI_API_KEY
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini client
genai.configure(api_key=GOOGLE_API_KEY)

# Use Gemini to generate answers
def generate_answer(query, context):
    prompt = f"""
You are a helpful chatbot. Answer the user's question using the context below. 
If you don't know, say you don't know.

Context:
{context}

Question:
{query}
"""

    model = genai.GenerativeModel("models/gemini-1.5-flash")


    response = model.generate_content(prompt)


    return response.text.strip()
