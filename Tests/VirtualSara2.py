import speech_recognition as sr
from selenium.common.exceptions import TimeoutException
from Functions.Talker import talk
import pywhatkit


def runSara(nameAV, engine):
    while True:
        sr.Microphone(device_index=0)
        
        # Creando un objeto de reconocimiento de voz
        r = sr.Recognizer()
        r.energy_threshold = 4000
        r.dynamic_energy_threshold = False

        with sr.Microphone() as source:
            print('Escuchando')
            talk('Te escucho', engine)

            # Reducir ruido
            r.adjust_for_ambient_noise(source)
            # Toma la voz de entrada desde el microfono
            audio = r.listen(source)
            try:
                phrase = r.recognize_google(audio, language='es-MX')
                phrase = phrase.lower()

                if nameAV in phrase:
                    phrase = phrase.replace(nameAV, '')
                
                if 'reproduce' in phrase:
                    music = phrase.replace('reproduce', '')
                    print("Reproduciendo " + music)
                    talk("Reproduciendo " + music, engine)
                    pywhatkit.playonyt(music)

                elif 'termina' in phrase:
                    talk("Adios", engine)
                    break
                
            except TimeoutException as msg:
                print(msg)
            except sr.WaitTimeoutError:
                print("El tiempo de espera ha finalizado.")
                quit()
            # speech is unintelligible
            except LookupError:
                print("No entendi lo que dijiste")
            else:
                print("Voz desde micrófono detectada.")
