import requests

bandera = True

def Telegram_Alert(mssg):
    while (bandera):
        send = 'Se ha detectado a: ' + mssg + 'by Sara'
        id = "-789572855" #Grupo a enviar
        token = "5048292664:AAFGCADK6IuFccuu5USne6vgZ8YGJpvtMsk" # Token BOT
        url = "https://api.telegram.org/bot" + token + "/sendMessage"
        params = {
            'chat_id': id,
            'text': send
        }
        requests.post(url, params = params)
        bandera = False
