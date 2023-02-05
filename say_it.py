import pyttsx3

engine = pyttsx3.init()


def say(text: str):
    engine.setProperty('voice', 'brazil')
    engine.say(text)
    engine.runAndWait()
