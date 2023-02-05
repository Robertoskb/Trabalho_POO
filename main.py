from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets, QtGui
from Interfaces.SpeakyNotes import Ui_Principal
from addnote import NotesWindow
from deletenotes import DeleteWindow
from help import HelpWindow
from about import AboutWindow
from itertools import cycle
from listnotes import ListWindow

from threading import Thread
from vb_functions import add_remind, delete_remind, list_reminds

import sys
import speech_recognition as sr


class MainWindow(QMainWindow, Ui_Principal):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.add_window = NotesWindow()
        self.delete_window = DeleteWindow()
        self.list_window = ListWindow()
        self.help_window = HelpWindow()
        self.about_window = AboutWindow()

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

        self.icons = cycle((QtGui.QIcon('images/352545_mic_off_icon.png'),
                            QtGui.QIcon('images/352475_mic_microphone_icon.png')))

        self.micButton.clicked.connect(lambda: self.set_mic(True))
        self.commands = {'adicionar lembrete': lambda: self.run_blind_function(add_remind),
                         'excluir lembrete': lambda: self.run_blind_function(delete_remind),
                         'exclui lembrete': lambda: self.run_blind_function(delete_remind),
                         'listar lembretes': lambda: self.run_blind_function(list_reminds)}

        self.mic = Thread(target=self.microphone)
        self.mic.start()

    def run_blind_function(self, func):
        self.mic_status = False
        func()
        self.mic_status = True

    def say_commands(self):
        pass

    def closeEvent(self, event):
        self.thread = False
        if self.mic_status:
            self.set_mic(False)
        super().closeEvent(event)

    def set_mic(self, change_colors):
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
        recognizer = sr.Recognizer()

        while self.thread:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)

                while self.mic_status:
                    print('gravando')
                    audio = recognizer.listen(source, phrase_time_limit=5)

                    try:
                        text = recognizer.recognize_google(audio, language='pt-BR')
                        if text == 'sair':
                            self.close()
                            sys.exit(app.exec_())

                        self.commands.get(text.lower(), lambda: print('não entendi'))()

                    except sr.UnknownValueError:
                        pass

    def connect_buttons(self):
        for button in self.buttons:
            button.setStyleSheet(button.style_on)
        self.addButton.clicked.connect(self.add_window.show)
        self.deleteButton.clicked.connect(self.delete_window.show)
        self.listButton.clicked.connect(self.list_window.show)
        self.helpButton.clicked.connect(self.help_window.show)
        self.aboutButton.clicked.connect(self.about_window.show)

        self.commandsButton.clicked.connect(self.say_commands)

    def disconnect_buttons(self):
        for button in self.buttons:
            button.clicked.disconnect()
            button.setStyleSheet(self.style_off)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
