import time
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from threading import Thread, Event
from datetime import datetime

stop_event = Event()

reminds = []


def set_clear(fun):
    def decoration(*args, **kwargs):
        stop_event.set()
        fun(*args, **kwargs)
        stop_event.clear()

    return decoration


class Reminder:

    def __init__(self, content: str, expiration: int, data):
        self.content = content
        self.expiration = expiration
        self.data = data


def add_remind():
    content = input('Conteudo: ')
    expiration = int(input('Tempo para expirar: '))
    data = datetime.now()

    reminds.append(Reminder(content, expiration, data))


def list_reminds():
    for c, remind in enumerate(reminds, 1):
        print(f'{c} - {remind.content} {remind.expiration} dia(s) para expirar')


commands = {'adcionar novo lembrete': add_remind, 'listar lembretes': list_reminds, 'sair': exit}


def microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        while not stop_event.is_set():
            print('gravando')
            audio = recognizer.listen(source, phrase_time_limit=5)

            try:
                text = recognizer.recognize_google(audio, language='pt-BR')

                commands.get(text, lambda: print('não entendi'))()

            except sr.UnknownValueError:
                pass


mic = Thread(target=microphone)
mic.start()

