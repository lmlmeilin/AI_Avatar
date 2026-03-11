from gtts import gTTS
import os

os.makedirs("examples", exist_ok=True)

text = "Li ho bo"

tts = gTTS(text=text, lang="zh")

tts.save("examples/example_input.wav")

print("example_input.wav created")