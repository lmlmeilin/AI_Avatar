import pyttsx3

engine = pyttsx3.init()

text = "How are you? Li hó bô?"

engine.save_to_file(text, "input.wav")
engine.runAndWait()

print("input.wav created")