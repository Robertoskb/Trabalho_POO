from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Interfaces.addWindow import Ui_notesWindow
from data.jsonhandler import JsonHandler
from datetime import datetime

file = JsonHandler('data/data.json')
data = file.read_json


class NotesWindow(QMainWindow, Ui_notesWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.confirmButton.clicked.connect(self.save_data)

    def save_data(self):
        content = self.textEdit.toPlainText()
        date = str(datetime.now())
        expiration = self.dateNumbers.value()

        if content.strip():
            data.append({'content': content.strip(), 'expiration': expiration, 'date': date})
            file.write_json(data)

            self.textEdit.setText('')
            self.dateNumbers.setValue(1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = NotesWindow()
    window.show()
    sys.exit(app.exec_())
