from mhs.mahasiswa import Mahasiswa
from ins.instansi import Instansi
# from klp.kelompok import kelompok
import klp.kelompok as kelompok
import os

def kelola_ins():
    # from instansi import Instansi
    host = "localhost" 
    user = "root"  
    password = ""  
    database = "pbl" 
    ins1 = Instansi(host,user,password,database)
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Pilihan operasi:")
        print("1. Insert Data Instansi ")
        print("2. Update Data Instansi")
        print("3. Delete Data Instansi")
        print("4. Tampil Data Instansi")
        print("5. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4): ")

        if choice == "1":
            nama = input("Masukkan nama Instansi: ")
            id = input("Masukkan id Instansi: ")
            alamat = input("Masukkan alamat Instansi: ")
            ins1.insert_mhs(nama, id, alamat)

        elif choice == "2":
            ins1.tampil_ins()
            id = input("Masukkan id Instansi yang akan diperbarui: ")
            nama_baru = input("Masukkan nama baru: ")
            alamat_baru = input("Masukkan alamat baru: ")
            ins1.update_mhs(id, nama_baru, alamat_baru)

        elif choice == "3":
            ins1.tampil_ins()
            id = input("Masukkan id Instansi yang akan dihapus: ")
            ins1.delete_mhs(id)

        elif choice == "4":
            ins1.tampil_ins()

        elif choice == "5":
            show_admin_menu()
            break
        
def kelola_mhs():
    host = "localhost" 
    user = "root"  
    password = ""  
    database = "pbl"  
    mhs1 = Mahasiswa(host, user, password, database)

    while True:
        print("Pilihan operasi:")
        print("1. Insert Data Mahasiswa ")
        print("2. Update Data Mahasiswa")
        print("3. Delete Data Mahasiswa")
        print("4. Tampil Data Mahasiswa")
        print("5. Kembali")

        choice = input("Masukkan pilihan (1/2/3/4): ")

        if choice == "1":
            nama = input("Masukkan nama mahasiswa: ")
            nim = input("Masukkan NIM mahasiswa: ")
            kelas = input("Masukkan kelas mahasiswa: ")
            mhs1.insert_mhs(nama, nim, kelas)

        elif choice == "2":
            mhs1.tampil_mhs()
            nim = input("Masukkan NIM mahasiswa yang akan diperbarui: ")
            nama_baru = input("Masukkan nama baru: ")
            kelas_baru = input("Masukkan kelas baru: ")
            mhs1.update_mhs(nim, nama_baru, kelas_baru)

        elif choice == "3":
            mhs1.tampil_mhs()
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            mhs1.delete_mhs(nim)

        elif choice == "4":
            mhs1.tampil_mhs()

        elif choice == "5":
            show_admin_menu()
            break

def show_admin_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("+"*5," Menu Admin ","+"*5)
    print("1. Kelola Data Mahasiswa")
    print("2. Kelola Data Instansi")
    print("3. Kelola Data kelompok")
    print("4. Kembali")
        
    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == "1":
        kelola_mhs()
    elif choice == "2":
        kelola_ins()
    elif choice == "3":
        kelompok.menu()
    elif choice == "4":
        SystemExit
