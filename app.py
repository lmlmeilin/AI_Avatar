import streamlit as st
from pathlib import Path
import subprocess
from PIL import Image
from gtts import gTTS

from llm_chat import ask_sealion

st.set_page_config(page_title="AI Avatar Chat", layout="centered")
st.title("🤖 AI Avatar Chat")

base_dir = Path(__file__).parent
results_dir = base_dir / "SadTalker/results"
results_dir.mkdir(parents=True, exist_ok=True)

# --- Upload avatar image ---
avatar_file = st.file_uploader("Upload avatar image (PNG/JPG)", type=["png", "jpg"])
avatar_path = base_dir / "avatar.png"

if avatar_file:
    with open(avatar_path, "wb") as f:
        f.write(avatar_file.getbuffer())
    image = Image.open(avatar_path)
    st.image(image, caption="Uploaded Avatar", width=200)

# --- Initialize session state for chat history ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # list of dicts: {"user": ..., "ai": ..., "video": ...}

# --- Chat input ---
st.subheader("Chat with your AI Avatar")
user_input = st.text_input("Type your message here:")

if st.button("Send"):
    if not avatar_file:
        st.error("Please upload an avatar image first!")
    elif not user_input.strip():
        st.error("Please type a message to send!")
    else:
        # --- Get AI text response ---
        st.info("Generating AI response...")
        try:
            response_text = ask_sealion(user_input)
        except Exception as e:
            st.error(f"Error generating LLM response: {e}")
            st.stop()

        # --- Convert AI response to audio ---
        st.info("Generating response audio... 🎵")
        response_wav_path = base_dir / "response.wav"
        try:
            tts = gTTS(text=response_text, lang="zh-tw")
            tts.save(str(response_wav_path))
        except Exception as e:
            st.error(f"Error generating TTS audio: {e}")
            st.stop()

        # --- Generate avatar video ---
        st.info("Generating avatar video... 🎬")
        try:
            subprocess.run([
                "python", "inference.py",
                "--driven_audio", str(response_wav_path),
                "--source_image", str(avatar_path),
                "--result_dir", str(results_dir)
            ], check=True, cwd=str(base_dir / "SadTalker"))
        except subprocess.CalledProcessError as e:
            st.error(f"Error generating video: {e}")
            st.stop()

        # --- Store the latest video path ---
        video_files = list(results_dir.glob("*.mp4"))
        latest_video = str(video_files[-1]) if video_files else None

        # --- Append to chat history ---
        st.session_state.chat_history.append({
            "user": user_input,
            "ai": response_text,
            "video": latest_video
        })

# --- Display chat history ---
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**AI Avatar:** {chat['ai']}")
    if chat['video']:
        st.video(chat['video'])
    st.markdown("---")