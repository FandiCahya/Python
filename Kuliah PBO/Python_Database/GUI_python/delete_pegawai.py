# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_pegawai.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pegawai import pegawai
from PyQt5.QtWidgets import QDialog

class Ui_Delete_Pegawai(object):
    def setupUi(self, Delete_Pegawai):
        self.Form = Delete_Pegawai
        Delete_Pegawai.setObjectName("Delete_Pegawai")
        Delete_Pegawai.resize(413, 415)
        self.label_judul = QtWidgets.QLabel(Delete_Pegawai)
        self.label_judul.setGeometry(QtCore.QRect(10, 10, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_judul.setFont(font)
        self.label_judul.setAlignment(QtCore.Qt.AlignCenter)
        self.label_judul.setObjectName("label_judul")
        self.label_nip = QtWidgets.QLabel(Delete_Pegawai)
        self.label_nip.setGeometry(QtCore.QRect(30, 80, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_nip.setFont(font)
        self.label_nip.setObjectName("label_nip")
        self.label_nama = QtWidgets.QLabel(Delete_Pegawai)
        self.label_nama.setGeometry(QtCore.QRect(30, 120, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_nama.setFont(font)
        self.label_nama.setObjectName("label_nama")
        self.label_hp = QtWidgets.QLabel(Delete_Pegawai)
        self.label_hp.setGeometry(QtCore.QRect(30, 160, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_hp.setFont(font)
        self.label_hp.setObjectName("label_hp")
        self.label_jabaatan = QtWidgets.QLabel(Delete_Pegawai)
        self.label_jabaatan.setGeometry(QtCore.QRect(30, 200, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_jabaatan.setFont(font)
        self.label_jabaatan.setObjectName("label_jabaatan")
        self.label_alamat = QtWidgets.QLabel(Delete_Pegawai)
        self.label_alamat.setGeometry(QtCore.QRect(30, 240, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_alamat.setFont(font)
        self.label_alamat.setObjectName("label_alamat")
        self.label_departemen = QtWidgets.QLabel(Delete_Pegawai)
        self.label_departemen.setGeometry(QtCore.QRect(30, 300, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_departemen.setFont(font)
        self.label_departemen.setObjectName("label_departemen")
        self.lineEdit_nip = QtWidgets.QLineEdit(Delete_Pegawai)
        self.lineEdit_nip.setGeometry(QtCore.QRect(130, 80, 201, 21))
        self.lineEdit_nip.setObjectName("lineEdit_nip")
        self.delete = QtWidgets.QPushButton(Delete_Pegawai)
        self.delete.setGeometry(QtCore.QRect(140, 360, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.delete.setFont(font)
        self.delete.setAutoFillBackground(False)
        self.delete.setObjectName("delete")
        self.kembali = QtWidgets.QPushButton(Delete_Pegawai)
        self.kembali.setGeometry(QtCore.QRect(30, 360, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kembali.setFont(font)
        self.kembali.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.kembali.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Kuliah/Semester 3/PBO/icon/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kembali.setIcon(icon)
        self.kembali.setIconSize(QtCore.QSize(20, 20))
        self.kembali.setObjectName("kembali")
        self.cari = QtWidgets.QPushButton(Delete_Pegawai)
        self.cari.setGeometry(QtCore.QRect(350, 80, 51, 23))
        self.cari.setObjectName("cari")
        self.nama = QtWidgets.QLabel(Delete_Pegawai)
        self.nama.setGeometry(QtCore.QRect(130, 120, 201, 21))
        self.nama.setFrameShape(QtWidgets.QFrame.Box)
        self.nama.setLineWidth(1)
        self.nama.setText("")
        self.nama.setWordWrap(False)
        self.nama.setObjectName("nama")
        self.hp = QtWidgets.QLabel(Delete_Pegawai)
        self.hp.setGeometry(QtCore.QRect(130, 160, 201, 21))
        self.hp.setFrameShape(QtWidgets.QFrame.Box)
        self.hp.setLineWidth(1)
        self.hp.setText("")
        self.hp.setWordWrap(False)
        self.hp.setObjectName("hp")
        self.jabatan = QtWidgets.QLabel(Delete_Pegawai)
        self.jabatan.setGeometry(QtCore.QRect(130, 200, 201, 21))
        self.jabatan.setFrameShape(QtWidgets.QFrame.Box)
        self.jabatan.setLineWidth(1)
        self.jabatan.setText("")
        self.jabatan.setWordWrap(False)
        self.jabatan.setObjectName("jabatan")
        self.alamat = QtWidgets.QLabel(Delete_Pegawai)
        self.alamat.setGeometry(QtCore.QRect(130, 240, 201, 41))
        self.alamat.setFrameShape(QtWidgets.QFrame.Box)
        self.alamat.setLineWidth(1)
        self.alamat.setText("")
        self.alamat.setWordWrap(False)
        self.alamat.setObjectName("alamat")
        self.label_5 = QtWidgets.QLabel(Delete_Pegawai)
        self.label_5.setGeometry(QtCore.QRect(130, 300, 201, 21))
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setLineWidth(1)
        self.label_5.setText("")
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Delete_Pegawai)
        QtCore.QMetaObject.connectSlotsByName(Delete_Pegawai)
        
        self.cari.clicked.connect(self.cariData)
        self.delete.clicked.connect(self.Deletedata)
        self.kembali.clicked.connect(self.kembalian)

    def retranslateUi(self, Delete_Pegawai):
        _translate = QtCore.QCoreApplication.translate
        Delete_Pegawai.setWindowTitle(_translate("Delete_Pegawai", "Insert Pegawai"))
        self.label_judul.setText(_translate("Delete_Pegawai", "Delete Pegawai "))
        self.label_nip.setText(_translate("Delete_Pegawai", "Nip"))
        self.label_nama.setText(_translate("Delete_Pegawai", "Nama"))
        self.label_hp.setText(_translate("Delete_Pegawai", "Hp"))
        self.label_jabaatan.setText(_translate("Delete_Pegawai", "Jabatan"))
        self.label_alamat.setText(_translate("Delete_Pegawai", "Alamat"))
        self.label_departemen.setText(_translate("Delete_Pegawai", "Departemen"))
        self.delete.setText(_translate("Delete_Pegawai", "Delete"))
        self.kembali.setText(_translate("Delete_Pegawai", ""))
        self.cari.setText(_translate("Delete_Pegawai", "Cari"))

    def cariData(self):
        nip = self.lineEdit_nip.text()
        data = pegawai.cari_data(nip)
        namaq = data[1]
        hpq = data[2]
        jabatanq = data[3]
        alamatq = data[4]
        departemenku = data[5]
        print(data)
        self.nama.setText(str(namaq))
        self.hp.setText(str(hpq))
        self.jabatan.setText(str(jabatanq))
        self.alamat.setText(str(alamatq))
        self.label_5.setText(str(departemenku))
        
    def Deletedata(self):
        nip = self.lineEdit_nip.text()
        pegawai.delete_data(nip)
        
        self.lineEdit_nip.clear()
        self.nama.clear()
        self.hp.clear()
        self.jabatan.clear()
        self.alamat.clear()
        self.label_5.clear()
        
    def kembalian(self):
        self.Form.close()
        
        from dashboard_pegawai import Ui_Dashboardpegawai
        self.dashboard_pegawai = QDialog()
        self.ui_dashboard_pegawai = Ui_Dashboardpegawai()
        self.ui_dashboard_pegawai.setupUi(self.dashboard_pegawai)
        self.dashboard_pegawai.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Delete_Pegawai = QtWidgets.QWidget()
    ui = Ui_Delete_Pegawai()
    ui.setupUi(Delete_Pegawai)
    Delete_Pegawai.show()
    sys.exit(app.exec_())