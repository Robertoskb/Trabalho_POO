from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Interfaces.aboutWindow import Ui_aboutWindow
import webbrowser


class AboutWindow(QMainWindow, Ui_aboutWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.links = (self.instaClarice, self.instaGrasielly, self.instaJackson,
                      self.instaDanilo, self.instaRoberto, self.instaLara)

        for label in self.links:
            label.setOpenExternalLinks(True)
            label.linkActivated.connect(webbrowser.open)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = AboutWindow()
    window.show()
    sys.exit(app.exec_())
