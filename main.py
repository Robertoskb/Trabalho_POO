from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets, QtGui
from Interfaces.SpeakyNotes import Ui_Principal
from addnote import NotesWindow
from deletenotes import DeleteWindow
from help import HelpWindow
from about import AboutWindow
from itertools import cycle
from listnotes import ListWindow
from say_it import say

from threading import Thread
from vb_functions import add_remind, delete_remind, list_reminds
from helpText_vblind import all_helps
from aboutText import about_text

import sys
import speech_recognition as sr

recognizer = sr.Recognizer()


class MainWindow(QMainWindow, Ui_Principal):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon('images/logo_speakynotes.png'))

        self.add_window = NotesWindow()
        self.delete_window = DeleteWindow()
        self.list_window = ListWindow()
        self.help_window = HelpWindow()
        self.about_window = AboutWindow()

        self.say_greetings = True
        self.say_quest = True

        self.buttons = [b for b in self.findChildren(QtWidgets.QPushButton)]
        self.buttons.remove(self.closeButton)
        self.buttons.remove(self.micButton)

        self.style_off = ("QPushButton{\n"
                          "    border-radius:10px;\n"
                          "    background-color: rgb(182, 182, 182);\n"
                          "    padding-top: 5px;\n"
                          "}\n")

        self.mic_style_on = self.micButton.styleSheet()

        for button in self.buttons:
            button.style_on = button.styleSheet()
            button.setStyleSheet(self.style_off)

        self.mic_status = True
        self.thread = True
        self.can_close = True

        self.icons = cycle((QtGui.QIcon('images/micOFF.png'),
                            QtGui.QIcon('images/micON.png')))

        commands_text = "para saber a função de cada comando listado a seguir, utilize o comando Ajuda. " \
                        "adicionar lembrete, excluir lembrete, listar lembretes, comandos, ajuda, sobre"
        self.micButton.clicked.connect(lambda: self.set_mic(True))
        self.commands = {'adicionar lembrete': lambda: self.run_blind_function(add_remind),
                         'excluir lembrete': lambda: self.run_blind_function(delete_remind),
                         'exclui lembrete': lambda: self.run_blind_function(delete_remind),
                         'listar lembretes': lambda: self.run_blind_function(list_reminds),
                         'comandos': lambda: self.run_blind_function(lambda: say(commands_text)),
                         'ajuda': lambda: self.run_blind_function(lambda: say(all_helps)),
                         'sobre': lambda: self.run_blind_function(lambda: say(about_text)),
                         'sair': self.close
                         }

        self.mic = Thread(target=self.microphone)
        self.mic.start()

    def run_blind_function(self, func):
        self.mic_status = False
        self.can_close = False
        func()
        self.mic_status = True
        self.say_quest = True
        self.can_close = True

    def closeEvent(self, event):
        if not self.can_close:
            event.ignore()

            return

        self.thread = False
        if self.mic_status:
            self.set_mic(False)
        self.close_windows()
        say('tchau, emoji de carainha feliz')
        super().closeEvent(event)

    def close_windows(self):
        windows = [self.add_window, self.delete_window, self.list_window,
                   self.help_window, self.about_window]

        for w in windows:
            try:
                w.close()

            except AttributeError:
                pass

    def set_mic(self, change_colors):
        if not self.can_close:
            return

        self.mic_status = not self.mic_status
        self.micButton.setIcon(next(self.icons))
        if self.mic_status:
            self.disconnect_buttons()
            self.micButton.setStyleSheet(self.mic_style_on)
        elif change_colors:
            self.connect_buttons()
            self.micButton.setStyleSheet("QPushButton{\n"
                                         "    border-radius:10px;\n"
                                         "    background-color: rgb(182, 182, 182);\n"
                                         "    padding-top: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "    background-color: rgb(198, 198, 198);\n"
                                         "    padding-top: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(198, 198, 198);\n"
                                         "    border-radius: 10px;\n"
                                         "    padding-top: -5px;\n")

    def microphone(self):
        while self.thread:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)

                while self.mic_status:
                    self.greetings()
                    audio = recognizer.listen(source, phrase_time_limit=5)

                    try:
                        text = recognizer.recognize_google(audio, language='pt-BR')

                        self.commands.get(text.lower(), lambda: print('não entendi'))()

                    except sr.UnknownValueError:
                        pass

    def greetings(self):
        if self.say_greetings:
            say('Bem vindo ao ispiqui noutes. Para aprender a como utilizar o programa fale "ajuda". '
                'Utilize fones de ouvido para uma melhor experiência')

            self.say_greetings = False

        if self.say_quest:
            say("o que você quer fazer hoje?")

            self.say_quest = False

    def connect_buttons(self):
        for button in self.buttons:
            button.setStyleSheet(button.style_on)
        self.addButton.clicked.connect(self.add_window.show)
        self.deleteButton.clicked.connect(self.delete_window.show)
        self.listButton.clicked.connect(self.list_window.show)
        self.helpButton.clicked.connect(self.help_window.show)
        self.aboutButton.clicked.connect(self.about_window.show)

        self.commandsButton.clicked.connect(lambda: say('adicionar lembrete, excluir lembrete, '
                                                        'listar lembretes, comandos, ajuda, sobre'))

    def disconnect_buttons(self):
        for button in self.buttons:
            button.clicked.disconnect()
            button.setStyleSheet(self.style_off)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
