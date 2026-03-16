from stt import transcribe
from hokkien_tts import speak
from llm_chat import ask_sealion

def run(audio_file: str):
    """
    Core AI loop:
    1. Transcribes audio to text.
    2. Sends text to AI brain.
    3. Speaks out the AI response.
    """
    # Convert audio to text
    user_text = transcribe(audio_file)
    print("User:", user_text)

    # Get AI response
    response = ask_sealion(user_text)
    print("AI:", response)

    # Convert AI response to speech
    speak(response)