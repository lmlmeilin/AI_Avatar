import streamlit as st
from backend.stt import transcribe_hokkien
from backend.llm import query_hokkien_llm
from backend.tts import synthesize_hokkien
from frontend.avatar import generate_avatar
from frontend.animation import animate_avatar
import os

st.title("Hokkien AI Avatar")

uploaded_audio = st.file_uploader("Speak to the Avatar (Hokkien)", type=["wav","mp3"])
if uploaded_audio:
    st.audio(uploaded_audio, format='audio/wav')
    st.info("Transcribing audio...")
    user_text = transcribe_hokkien(uploaded_audio)
    st.write(f"Transcribed: {user_text}")

    st.info("Generating Hokkien response...")
    response_text = query_hokkien_llm(user_text)
    st.write(f"LLM Response:\n{response_text}")

    st.info("Synthesizing speech...")
    audio_file = synthesize_hokkien(response_text, "response.wav")
    st.audio(audio_file)

    st.info("Generating avatar...")
    avatar_file = generate_avatar("friendly young person, talking, realistic", "avatar.jpg")
    
    st.info("Animating avatar...")
    video_file = animate_avatar(avatar_file, audio_file, "avatar_video.mp4")
    
    st.video(video_file)