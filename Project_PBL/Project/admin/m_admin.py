from sys import path

path.append('E:\Python\Project_PBL\Project')
import mahasiswa.f_mahasiswa as ms
import instansi.f_instansi as ins
import kelompok.f_kelompok as kel
# Fungsi utama untuk Admin
def admin_menu():
    while True:
        print("===== Menu Admin =====")
        print("1. Kelola Data Mahasiswa")
        print("2. Kelola Data Instansi")
        print("3. Kelola Data Kelompok")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            ms.menu_mahasiswa()
        elif pilihan == "2":
            ins.menu_instansi()
        elif pilihan == "3":
            kel.menu_kelompok()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi login Admin
def login_admin():
    username = input("Masukkan username Admin: ")
    password = input("Masukkan password Admin: ")  # Anda dapat mengimplementasikan autentikasi sesuai kebutuhan

    if username == "admin" and password == "admin":  # Gantilah dengan autentikasi yang sesuai
        admin_menu()
    else:
        print("Login gagal. Coba lagi.")