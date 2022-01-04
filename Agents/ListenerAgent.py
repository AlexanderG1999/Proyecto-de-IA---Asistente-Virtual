import speech_recognition as sr
import Agents.TalkerAgent

# Agente que escucha
def listen(listener, nameAV, engine):
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            Agents.TalkerAgent.talk("Te escucho", engine)
            pc = listener.listen(source)
            rec = listener.recognize_google(pc)
            rec = rec.lower()
            if nameAV in rec:
                rec = rec.replace(nameAV, '')
    except:
        pass
    return rec