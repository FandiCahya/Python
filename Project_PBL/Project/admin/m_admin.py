from sys import path

path.append('E:\Python\Project_PBL\Project')
from mahasiswa.f_mahasiswa1 import KelolaMahasiswa
from folder_instansi.f_instansi import KelolaInstansi
from kelompok.f_kelompok import MenuKelompok

class Admin:
    def __init__(self):
        pass

    def admin_menu(self):
        while True:
            print("===== Menu Admin =====")
            print("1. Kelola Data Mahasiswa")
            print("2. Kelola Data Instansi")
            print("3. Kelola Data Kelompok")
            print("4. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                km = KelolaMahasiswa()
                km.menu_mahasiswa()
            elif pilihan == "2":
                ks = KelolaInstansi()
                ks.menu_instansi()
            elif pilihan == "3":
                mk = MenuKelompok()
                mk.menu_kelompok()
            elif pilihan == "4":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def login_admin(self):
        username = input("Masukkan username Admin: ")
        password = input("Masukkan password Admin: ")  # Anda dapat mengimplementasikan autentikasi sesuai kebutuhan

        if username == "admin" and password == "admin":  # Gantilah dengan autentikasi yang sesuai
            self.admin_menu()
        else:
            print("Login gagal. Coba lagi.")

