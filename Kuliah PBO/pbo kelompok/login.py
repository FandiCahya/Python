# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import dashboard_admin as da
import dashboard_dosen as dd
import dashboard_mhs as dm
from User import User


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.dialog = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 160, 241, 141))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 160, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 240, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 190, 411, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 260, 411, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.login)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.label.setText(_translate("MainWindow", "USERNAME :"))
        self.label_2.setText(_translate("MainWindow", "PASSWORD :"))

    def openDA(self):
        self.dialog.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = da.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDM(self):
        self.dialog.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = dm.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openDS(self):
        self.dialog.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = dd.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        lvl_login = User.login(username, password)
        if lvl_login == "admin":
            self.openDA()
        elif lvl_login == "dosen":
            self.openDS()
        elif lvl_login == "mahasiswa":
            self.openDM()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
