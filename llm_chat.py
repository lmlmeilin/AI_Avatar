from ollama import chat

def ask_sealion(user_text):

    system_prompt = """
    You are a native Hokkien (Minnan) speaker and tutor.
    Speak naturally using Pe̍h-ōe-jī or Tailo romanization.
    Reply to user using one sentence only. 
    """

    response = chat(
        model="aisingapore/Llama-SEA-LION-v3.5-8B-R:latest",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":
    user_input = input("You: ")
    reply = ask_sealion(user_input)
    print("LLM:", reply)