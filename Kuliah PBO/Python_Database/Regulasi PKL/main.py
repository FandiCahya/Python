import mysql.connector
# from mhs.mahasiswa import Mahasiswa
# from ins.instansi import Instansi
import time
import adm
# from adm import show_admin_menu
from user import show_user_menu
import os
# Fungsi Login
def login(username, password):
    try:
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "pbl"
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        if result:
            print("Login berhasil!")
            return result
        else:
            print("Login gagal. Membuat pengguna baru.")
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
            time.sleep(0.5)
            print("Pengguna baru berhasil ditambahkan!")
            return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return result

if __name__ == "__main__":
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("="*7,"SISTEM INFORMASI REGULASI PKL","="*7)
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        log = login(username,password)
        print(log[-1])
        if log:
            if log[-1].lower() == "admin":
                adm.show_admin_menu()
                # show_admin_menu()
            elif log[-1].lower() == "user":
                show_user_menu()