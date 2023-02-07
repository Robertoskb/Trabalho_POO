from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Interfaces.addWindow import Ui_notesWindow
from data.jsonhandler import JsonHandler
from datetime import datetime
from say_it import say
from multiprocessing import Process

file = JsonHandler('data/data.json')


class NotesWindow(QMainWindow, Ui_notesWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon('images/logo_speakynotes.png'))

        self.confirmButton.clicked.connect(self.save_data)

    def save_data(self):
        data = file.read_json
        content = self.textEdit.toPlainText()
        date = str(datetime.now())
        expiration = self.dateNumbers.value()

        if content.strip():
            data.append({'content': content.strip(), 'expiration': expiration, 'date': date})
            file.write_json(data)

            self.textEdit.setText('')
            self.dateNumbers.setValue(1)
            Process(target=say, args=('Lembrete salvo com sucesso!',)).start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = NotesWindow()
    window.show()
    sys.exit(app.exec_())
