from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Interfaces.helpWindow import Ui_helpWindow
from say_it import say
import helpText


class HelpWindow(QMainWindow, Ui_helpWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon('images/logo_speakynotes.png'))

        self.helpSobre_Button.clicked.connect(lambda: say(helpText.aboutButton))
        self.helpAjuda_Button.clicked.connect(lambda: say(helpText.helpButton))
        self.helpComandos_Button.clicked.connect(lambda: say(helpText.commandButton))
        self.helpListar_Button.clicked.connect(lambda: say(helpText.list_reminderButton))
        self.helpExcluir_Button.clicked.connect(lambda: say(helpText.delete_reminderButton))
        self.helpAdicionar_Button.clicked.connect(lambda: say(helpText.add_reminderButton))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = HelpWindow()
    window.show()
    sys.exit(app.exec_())
