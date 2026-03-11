# tests/test_tts.py

import os
from backend.tts import synthesize_hokkien

TEST_TEXT = "Li ho bo, wa si AI avatar."


def test_tts_generation():
    audio_path = synthesize_hokkien(TEST_TEXT, "test_response.wav")

    assert os.path.exists(audio_path)
    assert audio_path.endswith(".wav")


if __name__ == "__main__":
    print("Testing TTS...")
    path = synthesize_hokkien(TEST_TEXT, "test_response.wav")
    print("Audio generated at:", path)