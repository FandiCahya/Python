import mysql.connector
import sys
import os

sys.path.append("E:\\Python\\Kuliah PBO\\Python_Database\\Regulasi PKL")
from mhs.mahasiswa import Mahasiswa
import adm

def insert_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbl"
    )
    mycursor = mydb.cursor()

    mhs1 = Mahasiswa("localhost", "root", "", "pbl")
    mhs1.tampil_mhs()
    
    kelompok_id = input("Masukkan ID kelompok: ")
    nama_kelompok = input("Masukkan nama kelompok: ")
    jml = int(input("Jumlah Anggota: "))
    
    anggota = []
    for i in range(jml):
        anggota.append(input(f"Masukkan anggota {i+1}: "))

    sql_kelompok = "INSERT INTO kelompok (id, nama_kelompok) VALUES (%s, %s)"
    val_kelompok = (kelompok_id, nama_kelompok)
    mycursor.execute(sql_kelompok, val_kelompok)

    sql_kelompok_mahasiswa = "INSERT INTO kelompok_mahasiswa (kelompok_id, anggota) VALUES (%s, %s)"
    val_kelompok_mahasiswa = [(kelompok_id, anggota[i]) for i in range(jml)]
    mycursor.executemany(sql_kelompok_mahasiswa, val_kelompok_mahasiswa)

    mydb.commit()
    print(mycursor.rowcount, "Data berhasil ditambahkan...")
    mydb.close()

def update_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbl"
    )
    mycursor = mydb.cursor()
    
    display_data()

    kelompok_id = input("Masukkan ID kelompok yang akan diupdate: ")
    nama_baru = input("Masukkan nama kelompok baru: ")

    sql = "UPDATE kelompok SET nama_kelompok = %s WHERE id = %s"
    val = (nama_baru, kelompok_id)
    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "Data kelompok berhasil diupdate...")
    mydb.close()

def delete_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbl"
    )
    mycursor = mydb.cursor()
    
    display_data()
    kelompok_id = input("Masukkan ID kelompok yang akan dihapus: ")

    sql = "DELETE FROM kelompok WHERE id = %s"
    val = (kelompok_id,)
    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "Data kelompok berhasil dihapus...")
    mydb.close()

def display_data():
    os.system("cls" if os.name == "nt" else "clear")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbl"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM kelompok")
    kelompok_result = mycursor.fetchall()
    print("Data Kelompok:")
    for row in kelompok_result:
        print(row)

    print("\nData Anggota:")
    for kelompok in kelompok_result:
        mycursor.execute("SELECT anggota FROM kelompok_mahasiswa WHERE kelompok_id = %s", (kelompok[0],))
        anggota_result = mycursor.fetchall()
        print(f"Anggota Kelompok {kelompok[0]}:")
        for anggota in anggota_result:
            print(anggota[0])

    mydb.close()

def menu():
    while True:
        print("Pilihan operasi:")
        print("1. Insert Data Kelompok")
        print("2. Update Data Kelompok")
        print("3. Delete Data Kelompok")
        print("4. Tampil Data Kelompok")
        print("5. Kembali")

        choice = input("Masukkan pilihan (1/2/3/4/5): ")
        if choice == "1":
            insert_data()
        elif choice == "2":
            update_data()
        elif choice == "3":
            delete_data()
        elif choice == "4":
            display_data()
        elif choice == "5":
            adm.show_admin_menu()
            
