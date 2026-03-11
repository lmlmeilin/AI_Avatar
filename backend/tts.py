from TTS.api import TTS
from config import TTS_MODEL_PATH, AUDIO_OUTPUT_DIR
import os

tts_model = TTS(TTS_MODEL_PATH)

def synthesize_hokkien(text: str, filename: str) -> str:
    output_path = os.path.join(AUDIO_OUTPUT_DIR, filename)
    tts_model.tts_to_file(text=text, file_path=output_path)
    return output_path