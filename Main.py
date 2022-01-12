import speech_recognition as sr
import pyttsx3

from Functions.VirtualSara import runSara

name = "Sara"
listener = sr.Recognizer()
engine = pyttsx3.init()  # Transforma texto a voz
voices = engine.getProperty('voices')# Se escoge una de las voces del sistema (Español)
engine.setProperty('voice', voices[0].id)

# Main
if __name__ == '__main__':
    runSara(listener, name, engine)
