import pyttsx3


def say(text: str):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'brazil')
    engine.say(text)
    engine.runAndWait()
