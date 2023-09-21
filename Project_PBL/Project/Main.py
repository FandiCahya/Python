from sys import path

path.append('E:\Python\Project_PBL\Project')
import os
import mahasiswa.f_mahasiswa as ms
# import instansi.f_instansi as ins
# import kelompok.f_kelompok as kel
import admin.m_admin as ad

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
        ad.login_admin()
    elif pilihan == "2":
        ms.login_mahasiswa()
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")