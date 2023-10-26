import time
import datetime
import os
import json
import Pemasukan,Pengeluaran

now = datetime.datetime.now()
dt = now.strftime("%d-%m-%Y %H:%M:%S")

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print("""Selamat datang di PMP2K
          
 _______  ____    ____  _______    _____   ___  ____   
|_   __ \|_   \  /   _||_   __ \  / ___ `.|_  ||_  _|  
  | |__) | |   \/   |    | |__) ||_/___) |  | |_/ /    
  |  ___/  | |\  /| |    |  ___/  .'____.'  |  __'.    
 _| |_    _| |_\/_| |_  _| |_    / /_____  _| |  \ \_  
|_____|  |_____||_____||_____|   |_______||____||____| 
                                                       
    (Program Monitoring Pemasukan dan Pengeluaran Keuangan) """)

def cek():
    try :
        with open("data.json","r") as data :
            if not data.read():
                print("file data.json kosong sedang membuat file \n")
                time.sleep(3)

                new_data = {
                    "pemasukan" : [],
                    "pengeluaran" : []
                }
                
                with open("data.json","w") as data :
                    json.dump(new_data,data)
                print("file data.json berhasil di buat")
                time.sleep(3)
            pass
    except:
        print("file data.json tidak di temukan sedang membuat file \n")
        time.sleep(3)

        new_data = {
            "pemasukan" : [],
            "pengeluaran" : []
        }
        
        with open("data.json","w") as data :
            json.dump(new_data,data)
        print("file data.json berhasil di buat")
        time.sleep(3)

def menu():
    banner()
    try:
        while True :
            print (""" 
            Menu Pilihan 
                1. Tambah Pemasukan
                2. Tambah Pengeluaran
                3. Monitoring Keuangan 
                4. keluar""")
            usr = int(input("Silahkan pilih menu : "))
            
            if usr > 4 or usr < 1:
                print("Masukan tidak valid pilih 1-4 ")
                continue

            if usr == 1:
                Pemasukan.Pemasukan.pemasukan()
            elif usr == 2:
                Pengeluaran.Pengeluaran.pengeluaran()
            elif usr == 3:
                Pemasukan.Pemasukan.lihat()
                Pengeluaran.Pengeluaran.lihat()
                break
            elif usr == 4:
                exit

            return usr            
    except:
        print("\nMasukan Harus berupa angka")
        menu()

if __name__ == "__main__":
    cek()
    menu()