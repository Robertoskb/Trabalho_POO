from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtWidgets
from Interfaces.deleteWindow import Ui_deleteWindow
from checkexpirations import check_expirations
from itertools import zip_longest
from datetime import datetime
from say_it import say
from data.jsonhandler import JsonHandler
import textwrap

file = JsonHandler('data/data.json')

data = check_expirations()
now = datetime.now()
data.sort(key=lambda d: d['expiration'] - (now - datetime.strptime(d['date'], r"%Y-%m-%d %H:%M:%S.%f")).days)
data_split = lambda: [data[i:i + 3] for i in range(0, len(data), 3)] or [[]]


def disconnect_button(button):
    try:
        button.clicked.disconnect()

    except TypeError:
        pass


class DeleteWindow(QMainWindow, Ui_deleteWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_page = 0

        self.data_split = data_split()
        self.pages_number = len(self.data_split)

        self.default_button_style = self.noteButton1.styleSheet()
        self.default_left_right_buttons_style = self.leftButton.styleSheet()

        self.buttons = (self.noteButton1, self.noteButton2, self.noteButton3)

        self.rename_buttons()

    def rename_buttons(self):
        rgbs = [('rgb(240, 83, 101)', 'rgb(230, 50, 50)'),
                ('rgb(52, 190, 78)', 'rgb(230, 50, 50)'),
                ('rgb(254, 160, 85)', 'rgb(230, 50, 50)')]

        for button, note, colors in zip_longest(self.buttons, self.data_split[self.current_page][:3], rgbs):
            if note:
                days = note['expiration']
                day_text = 'dias restantes' if days != 1 else 'dia restante'

                content = textwrap.fill(note['content'] + f' - ({days} {day_text})', 43)
                button.setText(content)
                button.setStyleSheet("QPushButton{\n"
                                     "    border-radius:10px;\n"
                                     f"    background-color: {colors[0]};\n"
                                     "    text-align: top left;\n"
                                     "    font-size: 20px;\n"
                                     "    word-wrap: break-word;\n"
                                     "    text-wrap: wrap;\n"
                                     "    padding: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     f"    background-color: {colors[1]};\n"
                                     "}"
                                     )

                button.mouseDoubleClickEvent = lambda state, content=content: say(content)
                button_id = int(button.objectName()[-1])
                button.clicked.connect(lambda state, button_id=button_id: self.delete_reminder(button_id))

            else:
                button.setText('slot')
                button.setStyleSheet(self.default_button_style)
                disconnect_button(button)

        self.check_pages()

    def delete_reminder(self, id_button):
        if self.reply() == QMessageBox.No:
            self.disconnect_buttons()
            self.rename_buttons()

            return

        index = (3 * self.current_page) + (id_button - 1)
        data.pop(index)
        self.data_split = data_split()
        self.pages_number = len(self.data_split)
        # file.write_json(data)

        if self.current_page != 0 and self.current_page > self.pages_number - 1:
            self.current_page -= 1

        self.disconnect_buttons()
        self.rename_buttons()

    def reply(self):
        reply = QMessageBox.question(QMainWindow(), 'Confirmação', 'Você tem certeza disso?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        return reply

    def disconnect_buttons(self):
        for button in self.buttons:
            disconnect_button(button)
        disconnect_button(self.leftButton)
        disconnect_button(self.rightButton)

    def check_pages(self):
        if self.current_page > 0:
            self.leftButton.setStyleSheet("QPushButton{\n"
                                          "    border-radius:10px;\n"
                                          "    \n"
                                          "    background-color: rgb(240, 83, 101);\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: rgb(254, 152, 177);\n"
                                          "}"
                                          )

            self.leftButton.clicked.connect(lambda: self.set_page(-1))

        else:
            self.leftButton.setStyleSheet(self.default_button_style)
            disconnect_button(self.leftButton)

        if self.current_page < self.pages_number - 1:
            self.rightButton.setStyleSheet("QPushButton{\n"
                                          "    border-radius:10px;\n"
                                          "    \n"
                                          "    background-color: rgb(240, 83, 101);\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: rgb(254, 152, 177);\n"
                                          "}")
            self.rightButton.clicked.connect(lambda: self.set_page(1))

        else:
            self.rightButton.setStyleSheet(self.default_button_style)
            disconnect_button(self.rightButton)

    def set_page(self, number):
        self.current_page += number
        self.rename_buttons()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = DeleteWindow()
    window.show()
    sys.exit(app.exec_())
