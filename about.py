from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtWidgets
from Interfaces.aboutWindow import Ui_aboutWindow
from say_it import say
from aboutText import about_text
from threading import Thread
import webbrowser


class AboutWindow(QMainWindow, Ui_aboutWindow):
    aboutToShow = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.aboutToShow.connect(lambda: Thread(target=lambda: say(about_text)).start())

        self.links = (self.instaClarice, self.instaGrasielly, self.instaJackson,
                      self.instaDanilo, self.instaRoberto, self.instaLara)

        for label in self.links:
            label.setOpenExternalLinks(True)
            label.linkActivated.connect(webbrowser.open)

    def show(self):
        super().show()
        try:
            self.aboutToShow.emit()
            
        except RuntimeError:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = AboutWindow()
    window.show()
    sys.exit(app.exec_())
