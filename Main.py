import speech_recognition as sr
import pyttsx3

from Agents.VirtualAgent import runJuan

name = "juan"
listener = sr.Recognizer()
engine = pyttsx3.init() # Transforma texto a voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # Se escoge una de las voces del sistema (Español)

# Main
if __name__ == '__main__':
    runJuan(listener, name, engine)
