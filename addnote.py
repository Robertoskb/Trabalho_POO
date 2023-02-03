from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Interfaces.addWindow import Ui_notesWindow
from data.jsonhandler import JsonHandler


file = JsonHandler('data/data.json')
data = file.read_json()


class MainWindow(QMainWindow, Ui_notesWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.confirmButton.clicked.connect()

    def save_data(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    notesWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(notesWindow)
    notesWindow.show()
    sys.exit(app.exec_())
