from sys import path

path.append('E:\Python\Project_PBL\Project')
import os
from mahasiswa.f_mahasiswa1 import KelolaMahasiswa
from admin.m_admin import Admin 

if __name__ == "__main__":
    sistem_operasi = os.name
# Program Utama
while True:
    match sistem_operasi:
        case "nt": os.system("cls")
    print("===== Sistem Informasi PKL =====")
    print("1. Login Admin")
    print("2. Login Mahasiswa")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        adm = Admin()
        adm.login_admin()
    elif pilihan == "2":
        km = KelolaMahasiswa()
        km.login_mahasiswa()
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")