from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Interfaces.addWindow import Ui_notesWindow
from data.jsonhandler import JsonHandler
from datetime import datetime

file = JsonHandler('data/data.json')
data = file.read_json()


class MainWindow(QMainWindow, Ui_notesWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.confirmButton.clicked.connect(self.save_data)

    def save_data(self):
        content = self.textEdit.toPlainText()
        date = str(datetime.now())
        expiration = self.dateNumbers.value()

        if content:
            data.append({'content': content, 'expiration': expiration, 'date': date})
            file.write_json(data)
            self.textEdit.setText('')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
