# Para que el AV hable
def talk(text, engine):
    engine.say(text)
    engine.runAndWait()