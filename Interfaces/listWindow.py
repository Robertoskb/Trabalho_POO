# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\listWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_listWindow(object):
    def setupUi(self, listWindow):
        listWindow.setObjectName("listWindow")
        listWindow.resize(464, 641)
        listWindow.setMinimumSize(QtCore.QSize(464, 641))
        listWindow.setMaximumSize(QtCore.QSize(464, 641))
        listWindow.setStyleSheet("background-color: rgb(244, 232, 157);")
        self.centralwidget = QtWidgets.QWidget(listWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.leftButton = QtWidgets.QPushButton(self.centralwidget)
        self.leftButton.setGeometry(QtCore.QRect(20, 540, 121, 81))
        self.leftButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"}\n"
"")
        self.leftButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Voltar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftButton.setIcon(icon)
        self.leftButton.setIconSize(QtCore.QSize(70, 70))
        self.leftButton.setObjectName("leftButton")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(170, 540, 121, 81))
        self.okButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(150, 193, 109);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(169, 225, 109);\n"
"}")
        self.okButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/okay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.okButton.setIcon(icon1)
        self.okButton.setIconSize(QtCore.QSize(40, 40))
        self.okButton.setObjectName("okButton")
        self.rightButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightButton.setGeometry(QtCore.QRect(320, 540, 121, 81))
        self.rightButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    \n"
"    background-color: rgb(182, 182, 182);\n"
"}\n"
"")
        self.rightButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/proximapag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rightButton.setIcon(icon2)
        self.rightButton.setIconSize(QtCore.QSize(80, 80))
        self.rightButton.setObjectName("rightButton")
        self.noteButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.noteButton1.setGeometry(QtCore.QRect(20, 20, 421, 161))
        self.noteButton1.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(252, 188, 184);\n"
"}")
        self.noteButton1.setObjectName("noteButton1")
        self.noteButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.noteButton2.setGeometry(QtCore.QRect(20, 190, 421, 161))
        self.noteButton2.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(252, 188, 184);\n"
"}")
        self.noteButton2.setObjectName("noteButton2")
        self.noteButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.noteButton3.setGeometry(QtCore.QRect(20, 360, 421, 161))
        self.noteButton3.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(252, 188, 184);\n"
"}")
        self.noteButton3.setObjectName("noteButton3")
        listWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(listWindow)
        self.okButton.clicked.connect(listWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(listWindow)

    def retranslateUi(self, listWindow):
        _translate = QtCore.QCoreApplication.translate
        listWindow.setWindowTitle(_translate("listWindow", "Listar Lembretes"))
        self.noteButton1.setText(_translate("listWindow", "Vazio"))
        self.noteButton2.setText(_translate("listWindow", "Vazio"))
        self.noteButton3.setText(_translate("listWindow", "Vazio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listWindow = QtWidgets.QMainWindow()
    ui = Ui_listWindow()
    ui.setupUi(listWindow)
    listWindow.show()
    sys.exit(app.exec_())
