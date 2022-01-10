import pywhatkit

import Functions.Listener
import Functions.Talker, os

from Functions.sendMail import sendMail

programs = {
    'telegram': "C:/Users/ASUS/AppData/Roaming/Telegram Desktop/Telegram.exe",
    'Microsoft Word': "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE",
    'onenote': "C:/Program Files/Microsoft Office/root/Office16/ONENOTE.EXE",
    'excel': "C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE",
    'whatsapp': "C:/Users/ASUS/AppData/Local/WhatsApp/WhatsApp.exe"
}

"""programs = {
    'telegram': "C:/Users/ASUS/AppData/Roaming/Telegram Desktop/Telegram.exe",
    'Microsoft Word': "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE",
    'onenote': "C:/Program Files/Microsoft Office/root/Office16/ONENOTE.EXE",
    'excel': "C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE",
    'whatsapp': "C:/Users/ASUS/AppData/Local/WhatsApp/WhatsApp.exe"
}"""


# Agente virtual
def runSara(listener, name, engine):
    while True:
        rec = Functions.Listener.listen(listener, name, engine)
        if 'play' in rec:
            music = rec.replace('play', '')
            print("Reproduciendo " + music)
            Functions.Talker.talk("Reproduciendo " + music, engine)
            pywhatkit.playonyt(music)
        elif 'open' in rec:
            for app in programs:
                if app in rec:
                    Functions.Talker.talk(f'Abriendo {app}', engine)
                    os.startfile(programs[app])
            print(f'Abriendo {app}')
        elif 'send' in rec:
            sendMail('alexanderguillin1999@gmail.com')
        elif 'finish' in rec:
            Functions.Talker.talk('Adios', engine)
            break