# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard_mahasiswa.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_logout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_logout.setGeometry(QtCore.QRect(349, 415, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setObjectName("btn_logout")
        self.btn_lihat_instansi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_lihat_instansi.setGeometry(QtCore.QRect(328, 294, 140, 39))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_lihat_instansi.setFont(font)
        self.btn_lihat_instansi.setObjectName("btn_lihat_instansi")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(5, 1, 779, 540))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:\Python\PBO KELOMPOK\gambar\mahasiswa (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.btn_logout.raise_()
        self.btn_lihat_instansi.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_logout.setText(_translate("MainWindow", "LOGOUT"))
        self.btn_lihat_instansi.setText(_translate("MainWindow", "Lihat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
