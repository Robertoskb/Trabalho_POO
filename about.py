from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Interfaces.aboutWindow import Ui_aboutWindow
from say_it import say
from aboutText import about_text
from multiprocessing import Process
import webbrowser


class AboutWindow(QMainWindow, Ui_aboutWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon('images/infoicon.png'))

        self.links = (self.instaClarice, self.instaGrasielly, self.instaJackson,
                      self.instaDanilo, self.instaRoberto, self.instaLara)

        for label in self.links:
            label.setOpenExternalLinks(True)
            label.linkActivated.connect(webbrowser.open)

    def show(self):
        super().show()
        Process(target=say, args=(about_text,)).start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = AboutWindow()
    window.show()
    sys.exit(app.exec_())
