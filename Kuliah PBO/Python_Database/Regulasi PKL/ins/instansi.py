# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="pbl"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE instansi (id VARCHAR(20) PRIMARY KEY, nama VARCHAR(55), alamat VARCHAR(55))")
import os

import mysql.connector

class Instansi:

    def __init__(self, host, user, password, database):
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pbl"
        )
        self.cursor = self.db_connection.cursor()

    def insert_ins(self, id, nama, alamat):
        try:
            sql = "INSERT INTO instansi (id, nama, alamat) VALUES (%s, %s, %s)"
            val = (id, nama, alamat)
            self.cursor.execute(sql, val)
            self.db_connection.commit()
            print("Data instansi berhasil ditambahkan!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def update_ins(self, id, nama_baru, alamat_baru):
        try:
            sql = "UPDATE instansi SET nama = %s, alamat = %s WHERE id = %s"
            val = (nama_baru, alamat_baru, id)
            self.cursor.execute(sql, val)
            self.db_connection.commit()
            print("Data instansi berhasil diperbarui!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def delete_ins(self, id):
        try:
            sql = "DELETE FROM instansi WHERE id = %s"
            val = (id,)
            self.cursor.execute(sql, val)
            self.db_connection.commit()
            print("Data instansi berhasil dihapus!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            
    def tampil_ins(self):
        os.system("cls" if os.name == "nt" else "clear")
        try:
            sql = "select * from instansi"
            self.cursor.execute(sql)
            myresult = self.cursor.fetchall()
            if len(myresult)>0:
                print("{:<5} {:<20} {:<50}".format('id', 'Nama', 'Alamat'))
                print("-" * 50)
                for row in myresult:
                    print("{:<5} {:<20} {:<50}".format(row[0], row[1], row[2]))
            else:
                print("Tidak Tersedia Data Mahasiswa")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def close_connection(self):
        self.cursor.close()
        self.db_connection.close()

