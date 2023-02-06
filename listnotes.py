from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from Interfaces.listWindow import Ui_listWindow
from say_it import say
from checkexpirations import check_expirations, parser_date
from itertools import zip_longest
from datetime import datetime
import textwrap


def disconnect_button(button):
    try:
        button.clicked.disconnect()

    except TypeError:
        pass


class ListWindow(QMainWindow, Ui_listWindow):
    aboutToShow = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.data_split = []
        self.current_page = self.pages_number = 0
        self.aboutToShow.connect(self.update)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(Qt.PointingHandCursor)

        self.default_button_style = self.noteButton1.styleSheet()
        self.default_left_right_buttons_style = self.leftButton.styleSheet()

        self.buttons = (self.noteButton1, self.noteButton2, self.noteButton3)

    def update(self):
        data = check_expirations()
        now = datetime.now()
        data.sort(key=lambda d: d['expiration'] - (now - datetime.strptime(d['date'], r"%Y-%m-%d %H:%M:%S.%f")).days)
        self.data_split = [data[i:i + 3] for i in range(0, len(data), 3)] or [[]]

        self.current_page = 0
        self.pages_number = len(self.data_split)

        self.rename_buttons()

    def closeEvent(self, event):
        self.disconnect_buttons()
        super().closeEvent(event)

    def show(self):
        self.aboutToShow.emit()
        super().show()

    def rename_buttons(self):
        rgbs = [('rgb(240, 83, 101)', 'rgb(253, 108, 111)'),
                ('rgb(52, 190, 78)', 'rgb(54, 215, 96)'),
                ('rgb(254, 160, 85)', 'rgb(254, 185, 85)')]

        for button, note, colors in zip_longest(self.buttons, self.data_split[self.current_page][:3], rgbs):
            if note:
                date = parser_date(note['date'])
                days = note['expiration']

                difference = days - (datetime.now() - date).days

                day_text = 'dias restantes' if difference != 1 else 'dia restante'

                content = note['content'] + f' - ({difference} {day_text})'

                button.setText(textwrap.fill(content, 43))
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
        self.disconnect_buttons()
        self.rename_buttons()

    def disconnect_buttons(self):
        for button in self.buttons:
            disconnect_button(button)
        disconnect_button(self.leftButton)
        disconnect_button(self.rightButton)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = ListWindow()
    window.show()
    sys.exit(app.exec_())
