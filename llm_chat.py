from ollama import chat

def ask_sealion(user_text):

    system_prompt = """
    You are a friendly chatbot. Reply queries with one sentence. 
    """

    response = chat(
        model="llama3.2:3b", #aisingapore/Llama-SEA-LION-v3.5-8B-R:latest
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