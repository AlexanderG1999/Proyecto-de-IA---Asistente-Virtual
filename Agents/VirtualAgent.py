import pywhatkit

import Agents.ListenerAgent
import Agents.TalkerAgent

# Agente virtual
def runJuan(listener, name, engine):
    rec = Agents.ListenerAgent.listen(listener, name)
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        print("Reproduciendo " + music)
        Agents.TalkerAgent.talk("Reproduciendo " + music, engine)
        pywhatkit.playonyt(music)