import speech_recognition as sr

# Agente que escucha
def listen(listener, nameAV):
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc)
            rec = rec.lower()
            if nameAV in rec:
                rec = rec.replace(nameAV, '')
    except:
        pass
    
    return rec