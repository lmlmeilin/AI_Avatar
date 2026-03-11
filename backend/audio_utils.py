import os
import uuid
from pydub import AudioSegment

# Default directories
AUDIO_DIR = "assets/audio"
TEMP_DIR = "assets/audio/temp"

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)


def generate_filename(prefix="audio", ext="wav"):
    """
    Generate a unique filename.
    """
    uid = uuid.uuid4().hex[:8]
    return f"{prefix}_{uid}.{ext}"


def save_uploaded_audio(uploaded_file):
    """
    Save Streamlit uploaded audio file to disk.
    """
    filename = generate_filename("user_input", "wav")
    path = os.path.join(TEMP_DIR, filename)

    with open(path, "wb") as f:
        f.write(uploaded_file.read())

    return path


def convert_to_wav(input_path, output_path=None):
    """
    Convert any audio format (mp3, m4a, etc.) to wav.
    """
    if output_path is None:
        output_path = input_path.rsplit(".", 1)[0] + ".wav"

    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="wav")

    return output_path


def resample_audio(input_path, target_rate=16000):
    """
    Resample audio for Whisper compatibility.
    Whisper works best with 16kHz WAV.
    """
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_frame_rate(target_rate)

    output_path = input_path.replace(".wav", "_16k.wav")
    audio.export(output_path, format="wav")

    return output_path


def cleanup_temp(folder=TEMP_DIR):
    """
    Delete temporary audio files.
    """
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        try:
            os.remove(path)
        except Exception:
            pass