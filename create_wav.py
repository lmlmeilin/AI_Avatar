import pyttsx3

engine = pyttsx3.init()

text = "Góa kin-á lâi chia̍h pn̄g, lí beh chia̍h bô?"

engine.save_to_file(text, "input.wav")
engine.runAndWait()

print("input.wav created")