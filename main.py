from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Interfaces.SpeakyNotes import Ui_Principal
from addnote import NotesWindow
from deletenotes import DeleteWindow
from help import HelpWindow

import sys

from listnotes import ListWindow


class MainWindow(QMainWindow, Ui_Principal):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.add_window = NotesWindow()
        self.delete_window = DeleteWindow()
        self.list_window = ListWindow()
        self.help_window = HelpWindow()

        self.addButton.clicked.connect(self.add_window.show)
        self.deleteButton.clicked.connect(self.delete_window.show)
        self.listButton.clicked.connect(self.list_window.show)
        self.helpButton.clicked.connect(self.help_window.show)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
