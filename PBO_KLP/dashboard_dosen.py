# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard_dosen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import login as l
import lihat_dsn_dsn as ld
import lihat_ints_dsn as li
import lihat_mhs_dsn as lm

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.dialog = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(3, 3, 791, 536))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:\Python\PBO KELOMPOK\gambar\dosen.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btn_logout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_logout.setGeometry(QtCore.QRect(110, 456, 122, 48))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setObjectName("btn_logout")
        self.btn_lihat_instansi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_lihat_instansi.setGeometry(QtCore.QRect(151, 195, 122, 48))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_lihat_instansi.setFont(font)
        self.btn_lihat_instansi.setObjectName("btn_lihat_instansi")
        self.btn_lihat_dosen = QtWidgets.QPushButton(self.centralwidget)
        self.btn_lihat_dosen.setGeometry(QtCore.QRect(528, 198, 122, 48))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_lihat_dosen.setFont(font)
        self.btn_lihat_dosen.setObjectName("btn_lihat_dosen")
        self.btn_lihat_mhs = QtWidgets.QPushButton(self.centralwidget)
        self.btn_lihat_mhs.setGeometry(QtCore.QRect(340, 420, 122, 48))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_lihat_mhs.setFont(font)
        self.btn_lihat_mhs.setObjectName("btn_lihat_mhs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn_logout.clicked.connect(self.logout)
        self.btn_lihat_dosen.clicked.connect(self.lihat_dosen)
        self.btn_lihat_instansi.clicked.connect(self.lihat_ins)
        self.btn_lihat_mhs.clicked.connect(self.lihat_mhs)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_logout.setText(_translate("MainWindow", "LOGOUT"))
        self.btn_lihat_instansi.setText(_translate("MainWindow", "LIHAT"))
        self.btn_lihat_dosen.setText(_translate("MainWindow", "LIHAT"))
        self.btn_lihat_mhs.setText(_translate("MainWindow", "LIHAT"))
        
    def logout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = l.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.dialog.close()
        
    def lihat_dosen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ld.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        self.dialog.close()
        
    def lihat_ins(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = li.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        self.dialog.close()
        
    def lihat_mhs(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = lm.Ui_Form()
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
