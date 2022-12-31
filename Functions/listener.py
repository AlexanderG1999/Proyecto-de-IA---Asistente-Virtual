import speech_recognition as sr
from selenium.common.exceptions import TimeoutException
from Functions.talker import talk

# AV escuche
def listen(nameAV, engine):
    sr.Microphone(device_index=0)

    # Creando un objeto de reconocimiento de voz
    r = sr.Recognizer()
    r.energy_threshold = 5000 # Mejorar calidad de reconocimiento de micrófono
    r.dynamic_energy_threshold = False

    with sr.Microphone() as source:
        talk('Te escucho', engine)
        print('Escuchando...')
        #r.pause_treshold = 0.1  # Evitar solapamiento de voces

        # Reducir ruido ambiental
        r.adjust_for_ambient_noise(source)
        # Toma la voz de entrada desde el microfono
        audio = r.listen(source)
        try:
            phrase = r.recognize_google(audio, language='es-MX')
            phrase = phrase.lower()

            if nameAV in phrase:
                phrase = phrase.replace(nameAV, '')
                
        except TimeoutException as msg:
            print(msg)
        except sr.WaitTimeoutError:
            talk('El tiempo de espera ha finalizado', engine)
            print("El tiempo de espera ha finalizado.")
            quit()
        # No se entendio la orden
        except LookupError:
            talk('No entendi lo que dijiste', engine)
            print("No entendi lo que dijiste")
        else:
            print("Voz desde micrófono detectada.")
    
    return phrase