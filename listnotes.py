from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Interfaces.listWindow import Ui_listWindow
from say_it import say
from checkexpirations import check_expirations
from itertools import zip_longest
from datetime import datetime
import textwrap


data = check_expirations()
now = datetime.now()
data.sort(key=lambda d: d['expiration'] - (now - datetime.strptime(d['date'], r"%Y-%m-%d %H:%M:%S.%f")).days)
data_split = [data[i:i+3] for i in range(0, len(data), 3)] or [[]]


def disconnect_button(button):
    try:
        button.clicked.disconnect()

    except TypeError:
        pass


class ListWindow(QMainWindow, Ui_listWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_page = 0
        self.pages_number = len(data_split)

        self.default_button_style = self.noteButton1.styleSheet()
        self.default_left_right_buttons_style = self.leftButton.styleSheet()

        self.buttons = (self.noteButton1, self.noteButton2, self.noteButton3)

        self.rename_buttons()

    def rename_buttons(self):
        rgbs = [('rgb(240, 83, 101)', 'rgb(253, 108, 111)'),
                ('rgb(52, 190, 78)', 'rgb(54, 215, 96)'),
                ('rgb(254, 160, 85)', 'rgb(254, 185, 85)')]

        for button, note, colors in zip_longest(self.buttons, data_split[self.current_page][:3], rgbs):
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

                button.clicked.connect(lambda state, content=content: say(content))

            else:
                button.setText('slot')
                button.setStyleSheet(self.default_button_style)
                disconnect_button(button)

        self.check_pages()

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
    window = ListWindow()
    window.show()
    sys.exit(app.exec_())
