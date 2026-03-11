import whisper
from config import STT_MODEL_PATH

stt_model = whisper.load_model("large-v3")  # or STT_MODEL_PATH

def transcribe_hokkien(audio_path: str) -> str:
    result = stt_model.transcribe(audio_path, language="zh", task="transcribe")
    return result["text"]