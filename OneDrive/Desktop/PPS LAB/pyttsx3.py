import pyttsx3

engine = pyttsx3.init()

# Set properties (optional but useful)
engine.setProperty('rate', 150)   # Speed of speech
engine.setProperty('volume', 1.0) # Volume (0.0 to 1.0)

# Speak text
engine.say("I will speak this text")
engine.runAndWait()