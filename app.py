import streamlit as st
from pathlib import Path
import subprocess
from PIL import Image

st.set_page_config(page_title="AI Avatar Generator", layout="centered")
st.title("🎤 AI Avatar Video Generator")

# Base directories
base_dir = Path(__file__).parent
results_dir = base_dir / "SadTalker/results"
results_dir.mkdir(parents=True, exist_ok=True)

# 1️⃣ Upload avatar image
avatar_file = st.file_uploader("Upload avatar image (PNG/JPG)", type=["png", "jpg"])
avatar_path = base_dir / "avatar.png"

if avatar_file:
    with open(avatar_path, "wb") as f:
        f.write(avatar_file.getbuffer())
    image = Image.open(avatar_path)
    st.image(image, caption="Uploaded Avatar", width=200)

# 2️⃣ Upload input audio
st.subheader("Upload your voice (WAV format)")
input_audio = st.file_uploader("Upload your voice (wav)", type=["wav"])
input_wav_path = base_dir / "input.wav"

if input_audio:
    with open(input_wav_path, "wb") as f:
        f.write(input_audio.getbuffer())
    st.success("Audio uploaded successfully!")

# 3️⃣ Generate AI Avatar Video
if st.button("Generate AI Avatar Video"):
    if not avatar_file:
        st.error("Please upload an avatar image first!")
    elif not input_audio:
        st.error("Please upload your audio first!")
    else:
        st.info("Generating response audio... 🎵")
        response_wav_path = base_dir / "response.wav"

        # Run test_run.py to generate response.wav
        try:
            subprocess.run(["python", "test_run.py"], check=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Error generating response audio: {e}")
            st.stop()

        st.info("Generating avatar video... 🎬")
        try:
            # Run inference.py inside the SadTalker folder to fix checkpoint paths
            subprocess.run([
                "python", "inference.py",
                "--driven_audio", str(response_wav_path),
                "--source_image", str(avatar_path),
                "--result_dir", str(results_dir)
            ], check=True, cwd=str(base_dir / "SadTalker"))
        except subprocess.CalledProcessError as e:
            st.error(f"Error generating video: {e}")
            st.stop()

        # Display generated video
        video_files = list(results_dir.glob("*.mp4"))
        if video_files:
            st.success("Video generated successfully! 🥳")
            st.video(str(video_files[-1]))
        else:
            st.error("Video generation failed.")