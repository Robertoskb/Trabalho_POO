from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Interfaces.helpWindow import Ui_helpWindow


class HelpWindow(QMainWindow, Ui_helpWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = HelpWindow()
    window.show()
    sys.exit(app.exec_())