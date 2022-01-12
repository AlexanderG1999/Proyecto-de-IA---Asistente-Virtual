import speech_recognition as sr
import Functions.Talker

# AV escuche
def listen(listener, nameAV, engine):
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            Functions.Talker.talk("Te escucho", engine)
            pc = listener.listen(source)  # Escuchar desde el microfono
            rec = listener.recognize_google(pc) # Utilizar servicios de reconocimiento de Google
            rec = rec.lower()
            
            if nameAV in rec:
                rec = rec.replace(nameAV, '')
                
    except:
        pass
    return rec
