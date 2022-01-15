from errno import ENFILE
import speech_recognition as sr
import pyttsx3

#from Functions.VirtualSara import runSara
from Functions.Listener import listen
from Tests.VirtualSara2 import runSara

name = 'sara'
#listener = sr.Recognizer()
#listener.energy_threshold = 5000
#listener.dynamic_energy_threshold = False
engine = pyttsx3.init()  # Transforma texto a voz
voices = engine.getProperty('voices')# Se escoge una de las voces del sistema (Español)
engine.setProperty('voice', voices[0].id)

# Main
if __name__ == '__main__':
    runSara(name, engine)
    #listen(name, engine)