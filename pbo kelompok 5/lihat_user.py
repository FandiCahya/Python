# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\lihat_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from User import User
import dashboard_user_admin as dua

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.cl = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 352)
        self.tableWidget = QtWidgets.QTableWidget(MainWindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 731, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(-20, 10, 261, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(360, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.kembali)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Level"))
        self.label.setText(_translate("Form", "DATA USERS"))
        self.pushButton.setText(_translate("Form", "Kembali"))

        data = self.lihat()
        row_count = len(data)

        self.tableWidget.setRowCount(row_count)
        
        for baris in range(row_count):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(baris, item)

            for kolom, value in enumerate(data[baris]):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(baris, kolom, item)

    def lihat(self):
        self.usr = User()
        a = self.usr.nilai()
        print(a)
        return a
    
    def kembali(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = dua.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.cl.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
