import speech_recognition as sr
import Functions.Talker

# AV escuche


def listen(listener, nameAV, engine):
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            Functions.Talker.talk("Te escucho", engine)
            listener.adjust_for_ambient_noise(source) #elimina el ruido de ambiente
            pc = listener.listen(source)  # Escuchar desde el microfono
            # Utilizar servicios de reconocimiento de Google
            rec = listener.recognize_google(pc, language='es-Mx') #ajuste de lenguaje
            rec = rec.lower()

            if nameAV in rec:
                rec = rec.replace(nameAV, '')

    except:
        pass
    return rec
