# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import instansi_admin as ia
import dosen_admin as da
import mahasiswa_admin as ma
import user_admin as ua
import login as l
import dashboard_klp_adm as k

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.dialog = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(640, 490, 121, 51))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 260, 151, 141))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(510, 260, 151, 141))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(150, 90, 151, 141))
        self.textEdit.setObjectName("textEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 30, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(510, 90, 151, 141))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_user = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_user.setGeometry(QtCore.QRect(180, 160, 91, 31))
        self.pushButton_user.setObjectName("pushButton_user")
        self.pushButton_instansi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_instansi.setGeometry(QtCore.QRect(540, 170, 91, 31))
        self.pushButton_instansi.setObjectName("pushButton_instansi")
        self.pushButton_dosen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dosen.setGeometry(QtCore.QRect(180, 340, 91, 31))
        self.pushButton_dosen.setObjectName("pushButton_dosen")
        self.pushButton_mahasiswa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mahasiswa.setGeometry(QtCore.QRect(540, 340, 91, 31))
        self.pushButton_mahasiswa.setObjectName("pushButton_mahasiswa")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(330, 370, 151, 141))
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 440, 91, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_dosen.clicked.connect(self.openDA)
        self.pushButton_user.clicked.connect(self.openUA)
        self.pushButton_logout.clicked.connect(self.logout)
        self.pushButton_6.clicked.connect(self.openK)
        self.pushButton_mahasiswa.clicked.connect(self.openMA)
        self.pushButton_instansi.clicked.connect(self.openIA)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_logout.setText(_translate("MainWindow", "LOGOUT"))
        # ... (other retranslateUi code)

    def openIA(self):
        self.dialog.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = ia.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openMA(self):
        self.dialog.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = ma.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openUA(self):
        self.dialog.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = ua.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDA(self):
        self.dialog.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = da.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openK(self):
        self.dialog.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = k.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def logout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = l.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.dialog.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
