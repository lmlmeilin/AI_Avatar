# test_tts.py
from hokkien_tts import speak

if __name__ == "__main__":
    test_text = "Lí kiò-mih miâ?"  # Example Hokkien phrase
    print(f"Speaking: {test_text}")
    speak(test_text)