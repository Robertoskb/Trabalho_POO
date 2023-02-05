# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SpeakyNotes2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(503, 687)
        Principal.setMinimumSize(QtCore.QSize(503, 687))
        Principal.setMaximumSize(QtCore.QSize(503, 687))
        Principal.setStyleSheet("background-color: rgb(244, 232, 157);")
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(30, 110, 211, 131))
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(240, 83, 101);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(253, 108, 111);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(253, 108, 111);\n"
"    border-radius: 10px;\n"
"    padding-top: -5px;\n"
"}")
        self.addButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Adicionar Lembrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QtCore.QSize(130, 130))
        self.addButton.setObjectName("addButton")
        self.micButton = QtWidgets.QPushButton(self.centralwidget)
        self.micButton.setGeometry(QtCore.QRect(30, 570, 211, 101))
        self.micButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.micButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(182, 182, 182);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(198, 198, 198);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(198, 198, 198);\n"
"    border-radius: 10px;\n"
"    padding-top: -5px;\n"
"}")
        self.micButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/352475_mic_microphone_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.micButton.setIcon(icon1)
        self.micButton.setIconSize(QtCore.QSize(60, 60))
        self.micButton.setObjectName("micButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(260, 570, 211, 101))
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(246, 11, 56);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(250, 43, 59);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(250, 43, 59);\n"
"    border-radius: 10px;\n"
"    padding-top: -5px;\n"
"}")
        self.closeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/sair.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QtCore.QSize(50, 50))
        self.closeButton.setObjectName("closeButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(260, 110, 211, 131))
        self.deleteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(255, 207, 87);\n"
"    padding-top: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 226, 106);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 226, 106);\n"
"    border-radius: 10px;\n"
"    padding-top: -5px;\n"
"}")
        self.deleteButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/Excluir Lembrete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon3)
        self.deleteButton.setIconSize(QtCore.QSize(120, 120))
        self.deleteButton.setObjectName("deleteButton")
        self.listButton = QtWidgets.QPushButton(self.centralwidget)
        self.listButton.setGeometry(QtCore.QRect(30, 260, 211, 131))
        self.listButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(52, 190, 78);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(54, 215, 96);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(54, 215, 96);\n"
"    border-radius: 10px;\n"
"    padding-top: -5px;\n"
"}")
        self.listButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/listar lembretes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.listButton.setIcon(icon4)
        self.listButton.setIconSize(QtCore.QSize(120, 120))
        self.listButton.setObjectName("listButton")
        self.commandsButton = QtWidgets.QPushButton(self.centralwidget)
        self.commandsButton.setGeometry(QtCore.QRect(260, 260, 211, 131))
        self.commandsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandsButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(162, 132, 151);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(162, 168, 206);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(162, 168, 206);\n"
"    border-radius: 10px;\n"
"    padding-top: -5px;\n"
"}")
        self.commandsButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/comandos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandsButton.setIcon(icon5)
        self.commandsButton.setIconSize(QtCore.QSize(120, 120))
        self.commandsButton.setObjectName("commandsButton")
        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setGeometry(QtCore.QRect(30, 410, 211, 131))
        self.helpButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(254, 160, 85);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(254, 185, 85);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 185, 85);\n"
"    border-radius: 10px;\n"
"    padding-top: -5px;\n"
"}")
        self.helpButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/Ajuda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon6)
        self.helpButton.setIconSize(QtCore.QSize(75, 75))
        self.helpButton.setObjectName("helpButton")
        self.aboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.aboutButton.setGeometry(QtCore.QRect(260, 410, 211, 131))
        self.aboutButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(121, 173, 220);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(121, 194, 220);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(121, 194, 220);\n"
"    border-radius: 10px;\n"
"    padding-top: -5px;\n"
"}")
        self.aboutButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/Sobre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutButton.setIcon(icon7)
        self.aboutButton.setIconSize(QtCore.QSize(75, 75))
        self.aboutButton.setObjectName("aboutButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 211, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/speakynotes.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 61, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/logo_speakynotes.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Principal)
        self.closeButton.clicked.connect(Principal.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())