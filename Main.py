from json.tool import main
from Functions.VirtualSara import runSara
import pyttsx3


name = 'sara'
engine = pyttsx3.init()  # Transforma texto a voz
voices = engine.getProperty('voices')# Se escoge una de las voces del sistema (Español)
engine.setProperty('voice', voices[0].id)


if __name__ == '__main__':
    runSara(name, engine)