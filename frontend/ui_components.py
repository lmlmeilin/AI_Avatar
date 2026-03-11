# frontend/ui_components.py

import streamlit as st


def render_header():
    """
    Display the main app title and description.
    """
    st.title("🗣️ Hokkien AI Avatar")
    st.markdown(
        "Talk to an AI avatar that understands and speaks **Hokkien (Minnan)**."
    )


def audio_input_component():
    """
    UI for uploading or recording audio.
    Returns uploaded audio file.
    """
    st.subheader("🎤 Speak to the Avatar")

    uploaded_audio = st.file_uploader(
        "Upload Hokkien audio",
        type=["wav", "mp3", "m4a"]
    )

    return uploaded_audio


def display_transcription(text):
    """
    Display STT transcription.
    """
    st.subheader("📝 Transcription")
    st.write(text)


def display_llm_response(response_text):
    """
    Show formatted SEA-LION response.
    """
    st.subheader("💬 AI Response")
    st.text(response_text)


def play_audio(audio_path):
    """
    Play generated TTS audio.
    """
    st.subheader("🔊 AI Voice")
    st.audio(audio_path, format="audio/wav")


def show_avatar_video(video_path):
    """
    Display generated talking avatar video.
    """
    st.subheader("🧑‍🎤 Avatar Response")
    st.video(video_path)


def show_processing(message):
    """
    Display processing spinner.
    """
    with st.spinner(message):
        st.write("Processing...")


def show_error(message):
    """
    Display error message.
    """
    st.error(message)


def show_success(message):
    """
    Display success message.
    """
    st.success(message)