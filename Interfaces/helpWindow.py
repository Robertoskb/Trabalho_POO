# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\helpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_helpWindow(object):
    def setupUi(self, helpWindow):
        helpWindow.setObjectName("helpWindow")
        helpWindow.resize(452, 364)
        helpWindow.setMinimumSize(QtCore.QSize(452, 364))
        helpWindow.setMaximumSize(QtCore.QSize(452, 364))
        helpWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        helpWindow.setStyleSheet("background-color: rgb(244, 232, 157);")
        self.centralwidget = QtWidgets.QWidget(helpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 121, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Ajuda.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.helpSobre_Button = QtWidgets.QPushButton(self.centralwidget)
        self.helpSobre_Button.setGeometry(QtCore.QRect(40, 100, 111, 111))
        self.helpSobre_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpSobre_Button.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(121, 173, 220);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(121, 194, 220);\n"
"}\n"
"\n"
"\n"
"")
        self.helpSobre_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Sobre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpSobre_Button.setIcon(icon)
        self.helpSobre_Button.setIconSize(QtCore.QSize(65, 65))
        self.helpSobre_Button.setObjectName("helpSobre_Button")
        self.helpAjuda_Button = QtWidgets.QPushButton(self.centralwidget)
        self.helpAjuda_Button.setGeometry(QtCore.QRect(170, 100, 111, 111))
        self.helpAjuda_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpAjuda_Button.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(254, 160, 85);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(254, 185, 85);\n"
"}\n"
"\n"
"")
        self.helpAjuda_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/Ajuda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpAjuda_Button.setIcon(icon1)
        self.helpAjuda_Button.setIconSize(QtCore.QSize(65, 65))
        self.helpAjuda_Button.setObjectName("helpAjuda_Button")
        self.helpComandos_Button = QtWidgets.QPushButton(self.centralwidget)
        self.helpComandos_Button.setGeometry(QtCore.QRect(300, 100, 111, 111))
        self.helpComandos_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpComandos_Button.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(162, 132, 151);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(162, 168, 206);\n"
"}\n"
"\n"
"")
        self.helpComandos_Button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/comandos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpComandos_Button.setIcon(icon2)
        self.helpComandos_Button.setIconSize(QtCore.QSize(95, 95))
        self.helpComandos_Button.setObjectName("helpComandos_Button")
        self.helpAdicionar_Button = QtWidgets.QPushButton(self.centralwidget)
        self.helpAdicionar_Button.setGeometry(QtCore.QRect(300, 230, 111, 111))
        self.helpAdicionar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpAdicionar_Button.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(240, 83, 101);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(253, 108, 111);\n"
"}\n"
"")
        self.helpAdicionar_Button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/Adicionar Lembrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpAdicionar_Button.setIcon(icon3)
        self.helpAdicionar_Button.setIconSize(QtCore.QSize(100, 100))
        self.helpAdicionar_Button.setObjectName("helpAdicionar_Button")
        self.helpListar_Button = QtWidgets.QPushButton(self.centralwidget)
        self.helpListar_Button.setGeometry(QtCore.QRect(40, 230, 111, 111))
        self.helpListar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpListar_Button.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(52, 190, 78);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(54, 215, 96);\n"
"}\n"
"")
        self.helpListar_Button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/listar lembretes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpListar_Button.setIcon(icon4)
        self.helpListar_Button.setIconSize(QtCore.QSize(100, 100))
        self.helpListar_Button.setObjectName("helpListar_Button")
        self.helpExcluir_Button = QtWidgets.QPushButton(self.centralwidget)
        self.helpExcluir_Button.setGeometry(QtCore.QRect(170, 230, 111, 111))
        self.helpExcluir_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpExcluir_Button.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(255, 207, 87);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 226, 106);\n"
"}\n"
"")
        self.helpExcluir_Button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/Excluir Lembrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpExcluir_Button.setIcon(icon5)
        self.helpExcluir_Button.setIconSize(QtCore.QSize(100, 100))
        self.helpExcluir_Button.setObjectName("helpExcluir_Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 20, 41, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/../Downloads/megafone.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.helpBack_Button = QtWidgets.QPushButton(self.centralwidget)
        self.helpBack_Button.setGeometry(QtCore.QRect(10, 20, 111, 51))
        self.helpBack_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpBack_Button.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(182, 182, 182);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(198, 198, 198);\n"
"}\n"
"")
        self.helpBack_Button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/Voltar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpBack_Button.setIcon(icon6)
        self.helpBack_Button.setIconSize(QtCore.QSize(50, 50))
        self.helpBack_Button.setObjectName("helpBack_Button")
        helpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(helpWindow)
        self.helpBack_Button.clicked.connect(helpWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(helpWindow)

    def retranslateUi(self, helpWindow):
        _translate = QtCore.QCoreApplication.translate
        helpWindow.setWindowTitle(_translate("helpWindow", "Ajuda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    helpWindow = QtWidgets.QMainWindow()
    ui = Ui_helpWindow()
    ui.setupUi(helpWindow)
    helpWindow.show()
    sys.exit(app.exec_())
