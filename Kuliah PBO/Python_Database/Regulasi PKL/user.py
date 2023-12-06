from mhs.mahasiswa import Mahasiswa
from ins.instansi import Instansi
from klp import kelompok
import os

def kelola_ins():
    # from instansi import Instansi
    host = "localhost" 
    user = "root"  
    password = ""  
    database = "pbl" 
    ins1 = Instansi(host,user,password,database)
    while True:
        # os.system("cls" if os.name == "nt" else "clear")
        print("Pilihan operasi:")
        print("1. Tampil Data Instansi")
        print("2. Kembali")

        choice = input("Masukkan pilihan (1/2): ")

        if choice == "1":
            ins1.tampil_ins()

        elif choice == "2":
            show_user_menu()
            break

        
def kelola_mhs():
    host = "localhost" 
    user = "root"  
    password = ""  
    database = "pbl"  
    mhs1 = Mahasiswa(host, user, password, database)

    while True:
        # os.system("cls" if os.name == "nt" else "clear")
        print("Pilihan operasi:")
        print("1. Tampil Data Mahasiswa")
        print("2. Kembali")

        choice = input("Masukkan pilihan (1/2): ")

        if choice == "1":
            mhs1.tampil_mhs()

        elif choice == "2":
            show_user_menu()
            break

def show_user_menu():
    print("+"*5," Menu User ","+"*5)
    print("1. Kelola Data Mahasiswa")
    print("2. Kelola Data Instansi")
    print("3. Lihat Data kelompok")
    print("4. Kembali")
        
    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == "1":
        kelola_mhs()
    elif choice == "2":
        kelola_ins()
    elif choice == "3":
        os.system("cls" if os.name == "nt" else "clear")
        kelompok.display_data()
        show_user_menu()
    elif choice == "4":
        SystemExit
