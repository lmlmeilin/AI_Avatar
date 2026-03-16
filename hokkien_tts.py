# hokkien_tts.py
import pyttsx3

# Initialize TTS engine once
engine = pyttsx3.init()

# Optional: choose a female voice if available
voices = engine.getProperty('voices')
for v in voices:
    if 'female' in v.name.lower():
        engine.setProperty('voice', v.id)
        break

def speak(text, filename="response.wav"):
    """
    Convert text to speech using pyttsx3 and save as WAV file.
    
    Args:
        text (str): Text to speak
        filename (str): Output WAV filename
    """
    # Save to file
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"Audio saved as {filename}")