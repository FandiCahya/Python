from time import time
from . import Database
import time
import os

def create_first_data():
    Nim = input("NIM : ")
    Nama_Mahasiswa = input("Nama Mahasiswa : ")
    Tempat_PKL = input("Tempat PKL : ")
    Date_PKL = input("Tanggal PKL : ")
    Lama_PKL = input("Lama PKL : ")
    Pembimbing = input("Nama Pembimbing : ")

    data = Database.TEMPLATE.copy()

    data["Nim"] = Nim + Database.TEMPLATE["Nim"][len(Nim):]
    data["Nama_Mahasiswa"] = Nama_Mahasiswa + Database.TEMPLATE["Nama_Mahasiswa"][len(Nama_Mahasiswa):]
    data["Tempat_PKL"] = Tempat_PKL + Database.TEMPLATE["Tempat_PKL"][len(Tempat_PKL):]
    data["date_PKL"] = Date_PKL + Database.TEMPLATE["Date_PKL"][len(Date_PKL):]
    data["Lama_PKL"] = Lama_PKL + Database.TEMPLATE["Lama_PKL"][len(Lama_PKL):]
    data["Pembimbing"] = Pembimbing + Database.TEMPLATE["pembimbing"][len(Pembimbing):]

    data_str = f'{data["Nim"]},{data["Nama_Mahasiswa"]},{data["Tempat_PKL"]},{data["date_PKL"]},{data["Lama_PKL"]},{data["Pembimbing"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah lah Gagal booooos")

def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("Membaca database error")
        return False