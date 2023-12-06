# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_edit_data_barang.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Barang import Barang
from kategori import kategori
from PyQt5.QtWidgets import QDialog


class Ui_edit(object):
    def setupUi(self, Dialog):
        self.Form = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(643, 386)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.comboBox_kategori = QtWidgets.QComboBox(Dialog)
        self.comboBox_kategori.setGeometry(QtCore.QRect(230, 220, 191, 22))
        self.comboBox_kategori.setObjectName("comboBox_kategori")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 180, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(180, 220, 47, 13))
        self.label_5.setObjectName("label_5")
        self.btn_update = QtWidgets.QPushButton(Dialog)
        self.btn_update.setGeometry(QtCore.QRect(320, 260, 75, 23))
        self.btn_update.setObjectName("btn_update")
        self.btn_kembali = QtWidgets.QPushButton(Dialog)
        self.btn_kembali.setGeometry(QtCore.QRect(220, 260, 75, 23))
        self.btn_kembali.setObjectName("btn_kembali")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 140, 47, 13))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_id = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_id.setGeometry(QtCore.QRect(230, 60, 113, 20))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_nama = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nama.setGeometry(QtCore.QRect(230, 100, 191, 20))
        self.lineEdit_nama.setObjectName("lineEdit_nama")
        self.lineEdit_stock = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_stock.setGeometry(QtCore.QRect(230, 140, 191, 20))
        self.lineEdit_stock.setObjectName("lineEdit_stock")
        self.lineEdit_harga = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_harga.setGeometry(QtCore.QRect(230, 180, 191, 20))
        self.lineEdit_harga.setObjectName("lineEdit_harga")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(180, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.getDataCategori()
        
        self.pushButton.clicked.connect(self.cariData)
        self.btn_update.clicked.connect(self.UpdateData)
        self.btn_kembali.clicked.connect(self.kembali)
        
    def getDataCategori(self):
        data = kategori.select_data()
        print(data)
        self.comboBox_kategori.addItems(data)
        
    def cariData(self):
        id = self.lineEdit_id.text()
        data = Barang.select_data_by_id(id)
        nama = data[1]
        stok = data[2]
        harga = data[3]
        kategori = data[4]
        self.lineEdit_nama.setText(str(nama))
        self.lineEdit_stock.setText(str(stok))
        self.lineEdit_harga.setText(str(harga))
        self.comboBox_kategori.setCurrentText(str(kategori))
        
    def UpdateData(self):
        id_to_update = self.lineEdit_id.text()
        new_nama = self.lineEdit_nama.text()
        new_stok = self.lineEdit_stock.text()
        new_harga = self.lineEdit_harga.text()
        new_kategori = self.comboBox_kategori.currentText()
        Barang.update_data(new_nama, new_stok, new_harga, new_kategori,id_to_update)
        
        self.lineEdit_id.clear()
        self.lineEdit_nama.clear()
        self.lineEdit_stock.clear()
        self.lineEdit_harga.clear()
        self.comboBox_kategori.clear()

    def kembali(self):
        self.Form.close()
        
        from dashboard_kasir import Ui_DashboardKasir
        self.dashboard_kasir = QDialog()
        self.ui_dashboard_kasir = Ui_DashboardKasir()
        self.ui_dashboard_kasir.setupUi(self.dashboard_kasir)
        self.dashboard_kasir.show()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Nama"))
        self.label_2.setText(_translate("Dialog", "ID"))
        self.label_4.setText(_translate("Dialog", "Harga"))
        self.label_5.setText(_translate("Dialog", "Kategori"))
        self.btn_update.setText(_translate("Dialog", "UPDATE"))
        self.btn_kembali.setText(_translate("Dialog", "KEMBALI"))
        self.label.setText(_translate("Dialog", "Stok"))
        self.pushButton.setText(_translate("Dialog", "Cari"))
        self.label_6.setText(_translate("Dialog", "Edit Data Barang"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_edit()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
