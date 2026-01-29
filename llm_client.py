"""
llm_client.py
Handles communication with OpenAI for Jarvis AI responses.
"""

import os
from openai import OpenAI

# OpenAI client uses API key from environment variable
client = OpenAI()

SYSTEM_PROMPT = """
You are Jarvis, a transportation assistance robot.
You were developed by Naman Kedia and Mayank Agarwal.

Guidelines:
- Be concise
- Be calm and helpful
- Prefer short, clear spoken responses
- Never give unsafe instructions
- Never encourage harmful or dangerous behavior
"""

def ask_llm(user_text: str) -> str:
    """
    Sends user text to the LLM and returns a short response.
    Safe for spoken output.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ],
            max_tokens=80
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("LLM error:", e)
        return "Sorry, I am currently offline."
