import subprocess
from config import VIDEO_OUTPUT_DIR

def animate_avatar(avatar_image: str, audio_file: str, output_name: str) -> str:
    output_path = f"{VIDEO_OUTPUT_DIR}/{output_name}"
    # Example: using SadTalker CLI
    cmd = [
        "python", "SadTalker/inference.py",
        "--driven_audio", audio_file,
        "--source_image", avatar_image,
        "--result_path", output_path
    ]
    subprocess.run(cmd, check=True)
    return output_path