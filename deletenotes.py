from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtWidgets
from Interfaces.deleteWindow import Ui_deleteWindow
from checkexpirations import check_expirations, parser_date
from itertools import zip_longest
from datetime import datetime
from say_it import say
from data.jsonhandler import JsonHandler
import textwrap

file = JsonHandler('data/data.json')

data_split = lambda data: [data[i:i + 3] for i in range(0, len(data), 3)] or [[]]


def disconnect_button(button):
    try:
        button.clicked.disconnect()

    except TypeError:
        pass


def message_box():
    msg_box = QMessageBox()
    msg_box.setWindowIcon(QIcon('images/lixeira.png'))
    msg_box.setText('Você em certeza disso?')
    msg_box.setWindowTitle('confirmação')
    confirm_btn = msg_box.addButton('Sim', QMessageBox.YesRole)
    _ = msg_box.addButton('Não', QMessageBox.NoRole)

    msg_box.exec_()

    if msg_box.clickedButton() == confirm_btn:
        return True
    return False


class DeleteWindow(QMainWindow, Ui_deleteWindow):
    aboutToShow = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.aboutToShow.connect(self.update)

        self.setWindowIcon(QIcon('images/logo_speakynotes.png'))

        self.current_page = self.pages_number = 0
        self.data_split = self.data = None

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(Qt.PointingHandCursor)

        self.default_button_style = self.noteButton1.styleSheet()
        self.default_left_right_buttons_style = self.leftButton.styleSheet()

        self.buttons = (self.noteButton1, self.noteButton2, self.noteButton3)

    def update(self):
        data = check_expirations()
        now = datetime.now()
        data.sort(key=lambda x: x['expiration'] - (now - datetime.strptime(x['date'], r"%Y-%m-%d %H:%M:%S.%f")).days)

        self.data = data
        self.data_split = data_split(data)
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
        rgbs = [('rgb(240, 83, 101)', 'rgb(230, 50, 50)'),
                ('rgb(52, 190, 78)', 'rgb(230, 50, 50)'),
                ('rgb(254, 160, 85)', 'rgb(230, 50, 50)')]

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

                button.mouseDoubleClickEvent = lambda state, content=content: say(content)
                button_id = int(button.objectName()[-1])
                button.clicked.connect(lambda state, button_id=button_id: self.delete_reminder(button_id))

            else:
                button.setText('slot')
                button.setStyleSheet(self.default_button_style)
                disconnect_button(button)

        self.check_pages()

    def delete_reminder(self, id_button):
        if not message_box():
            self.disconnect_buttons()
            self.rename_buttons()

            return

        index = (3 * self.current_page) + (id_button - 1)
        self.data.pop(index)
        self.data_split = data_split(self.data)
        self.pages_number = len(self.data_split)
        file.write_json(self.data)

        if self.current_page != 0 and self.current_page > self.pages_number - 1:
            self.current_page -= 1

        self.disconnect_buttons()
        self.rename_buttons()

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
