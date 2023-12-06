# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dalate_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from User import User
from PyQt5.QtWidgets import QDialog

class Ui_delete(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label_pw = QtWidgets.QLabel(Form)
        self.label_pw.setGeometry(QtCore.QRect(40, 150, 47, 13))
        self.label_pw.setObjectName("label_pw")
        self.L_lv = QtWidgets.QLineEdit(Form)
        self.L_lv.setGeometry(QtCore.QRect(150, 200, 201, 20))
        self.L_lv.setReadOnly(True)
        self.L_lv.setObjectName("L_lv")
        self.label_username_2 = QtWidgets.QLabel(Form)
        self.label_username_2.setGeometry(QtCore.QRect(40, 60, 47, 13))
        self.label_username_2.setObjectName("label_username_2")
        self.L_pw = QtWidgets.QLineEdit(Form)
        self.L_pw.setGeometry(QtCore.QRect(150, 150, 201, 20))
        self.L_pw.setReadOnly(True)
        self.L_pw.setObjectName("L_pw")
        self.label_nama = QtWidgets.QLabel(Form)
        self.label_nama.setGeometry(QtCore.QRect(40, 100, 47, 13))
        self.label_nama.setObjectName("label_nama")
        self.L_username = QtWidgets.QLineEdit(Form)
        self.L_username.setGeometry(QtCore.QRect(150, 100, 201, 20))
        self.L_username.setReadOnly(True)
        self.L_username.setObjectName("L_username")
        self.label_lv = QtWidgets.QLabel(Form)
        self.label_lv.setGeometry(QtCore.QRect(40, 200, 47, 13))
        self.label_lv.setObjectName("label_lv")
        self.L_nama = QtWidgets.QLineEdit(Form)
        self.L_nama.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.L_nama.setObjectName("L_nama")
        self.update = QtWidgets.QPushButton(Form)
        self.update.setGeometry(QtCore.QRect(240, 240, 100, 41))
        self.kembali = QtWidgets.QPushButton(Form)
        self.kembali.setGeometry(QtCore.QRect(70, 240, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.update.setFont(font)
        self.update.setObjectName("update")
        self.kembali.setFont(font)
        self.kembali.setObjectName("kembali")
        self.label_judul = QtWidgets.QLabel(Form)
        self.label_judul.setGeometry(QtCore.QRect(120, 10, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_judul.setFont(font)
        self.label_judul.setObjectName("label_judul")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.pushButton.clicked.connect(self.cari)
        self.update.clicked.connect(self.delete_data)
        self.kembali.clicked.connect(self.btnkembali)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Delete User"))
        self.label_pw.setText(_translate("Form", "password"))
        self.label_username_2.setText(_translate("Form", "username"))
        self.label_nama.setText(_translate("Form", "nama"))
        self.label_lv.setText(_translate("Form", "level"))
        self.update.setText(_translate("Form", "Delete"))
        self.kembali.setText(_translate("Form", "Kembali"))
        self.label_judul.setText(_translate("Form", "Delete data user"))
        self.pushButton.setText(_translate("Form", "cari"))

    def cari(self):
        self.usr = User
        
        username = self.L_nama.text()
        
        myresult = self.usr.cari_data(username)
        
        print(myresult)
        self.L_username.setText(myresult[0])
        self.L_pw.setText(myresult[2])
        self.L_lv.setText(myresult[-1])

    def delete_data(self):
        username_baru = self.L_nama.text()
        User.delete_data(username_baru)
        
        self.L_username.clear()
        self.L_nama.clear()
        self.L_pw.clear()
        self.L_pw.clear()
        
    def btnkembali(self):
        self.Form.close()
        
        from dashboard_admin import Ui_DashboardAdmin
        self.dashboard_kasir = QDialog()
        self.ui_dashboard_kasir = Ui_DashboardAdmin()
        self.ui_dashboard_kasir.setupUi(self.dashboard_kasir)
        self.dashboard_kasir.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_delete()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
