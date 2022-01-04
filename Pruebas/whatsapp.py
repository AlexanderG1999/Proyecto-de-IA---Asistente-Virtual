# Importamos el ModuMódulo

import pywhatkit

# Usamos Un try-except
try:

  # Enviamos el mensaje

  pywhatkit.sendwhatmsg("+593996132210",
                        "Mensaje De Prueba",
                        16,10)

  print("Mensaje Enviado")

except:

  print("Ocurrio Un Error")