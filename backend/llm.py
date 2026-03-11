from ollama import chat
from config import SEA_LION_MODEL

SYSTEM_PROMPT = """
You are a native Hokkien (Minnan) speaker and tutor. Speak naturally using Pe̍h-ōe-jī or Tailo romanization; Chinese characters optional. 
Use natural particles like lah, leh, liao, meh, hor, boh. Respond in this format:
Hokkien: <sentence>
Romanization: <romanization>
English: <translation>
Explanation (optional): <short explanation>
"""

def query_hokkien_llm(user_text: str) -> str:
    response = chat(
        model=SEA_LION_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ]
    )
    return response["message"]["content"]