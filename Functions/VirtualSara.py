import pywhatkit

from Functions.listener import listen
from Functions.talker import talk
from Functions.createEvent import create_event
import os
import subprocess

from Functions.sendMail import sendMail


def escribirArchivo(cadena, rutaArchivo):
    archivo = open(rutaArchivo, "a")
    archivo.write(cadena+'\n')
    archivo.close()


# Agente virtual
def runSara(name, engine):
    while True:
        rec = listen(name, engine)
        
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo " + music)
            talk("Reproduciendo " + music, engine)
            pywhatkit.playonyt(music)
        
        elif 'abre' in rec:
            cmd = ['hostname']
            shell_cmd = subprocess.run((cmd), capture_output=True, text=True)
            hostname = (shell_cmd.stdout).rstrip()

            if hostname == "ALEXANDER": #Computadora Alexander
                archivo = "Files/programsAlex.txt"
            else: #Computadora Leo
                archivo = "Files/programsLeo.txt"

            with open(archivo) as programs:
                for linea in programs:
                    linea = linea.split(': ')
                    if linea[0] in rec:
                        talk(f'Abriendo {linea[0]}', engine)
                        os.startfile(linea[1].rstrip())
                        print(f'Abriendo {linea[0]}')
        
        elif 'enviar email' in rec:
            talk(f'Enviando email', engine)
            sendMail(name, engine)

        elif 'crear evento en el calendario' in rec:
            talk('Creando evento', engine)
            print('Creando evento...')
            create_event(name, engine)
        
        elif 'termina' in rec:
            talk('Adios', engine)
            break
