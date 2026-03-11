import pyttsx3

engine = pyttsx3.init()

text = "Li Ho Bo"

engine.save_to_file(text, "input.wav")
engine.runAndWait()

print("input.wav created")