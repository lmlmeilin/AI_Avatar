from backend.stt import transcribe_hokkien

TEST_AUDIO = "examples/example_input.wav"


def test_stt_transcription():
    text = transcribe_hokkien(TEST_AUDIO)

    assert text is not None
    assert isinstance(text, str)
    assert len(text) > 0


if __name__ == "__main__":
    print("Testing Whisper STT...")
    result = transcribe_hokkien(TEST_AUDIO)
    print("Transcription:", result)