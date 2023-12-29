import mysql.connector

db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbl"
)
cursor = db_connection.cursor()

class Kelompok:

    def __init__(self):
        self

    def tampil (self):
        sql = "select * from kelompok"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        return myresult
    
    def cari_data (id):
        sql = "SELECT id, nama, ketua, anggota_1, anggota_2, instansi, dosen FROM kelompok where id = %s "
        val = (id,)
        cursor.execute(sql,val)
        myresult = cursor.fetchone()
        return myresult
    
    def select_data():
        sql = "SELECT * FROM kelompok"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)

    def insert_kelompok(id, nama, ketua, anggota_1, anggota_2, instansi, dosen):
        try:
            sql = "INSERT INTO kelompok (id, nama, ketua, anggota_1, anggota_2, instansi, dosen) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (id, nama, ketua, anggota_1, anggota_2, instansi, dosen)
            cursor.execute(sql, val)
            db_connection.commit()
            print(cursor.rowcount, "Data kelompok berhasil ditambahkan...")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def update_kelompok(val1,val2,val3,val4,val5,val6,val7):
        try:
            sql = "UPDATE kelompok SET nama = %s, ketua = %s, anggota_1 = %s, anggota_2 = %s, instansi = %s, dosen = %s WHERE id = %s"
            val = (val1,val2,val3,val4,val5,val6,val7)
            cursor.execute(sql, val)
            db_connection.commit()
            print(cursor.rowcount, "Data kelompok berhasil diperbarui...")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def delete_kelompok(id):
        try:
            sql = "DELETE FROM kelompok WHERE id = %s"
            val = (id,)
            cursor.execute(sql, val)
            db_connection.commit()
            print(cursor.rowcount, "Data kelompok berhasil dihapus...")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def select_data_by_id(val1):
        sql = "SELECT id, nama, ketua, anggota_1, anggota_2, instansi, dosen FROM kelompok WHERE id = %s"
        val = (val1)
        cursor.execute(sql,val)
        myresult = cursor.fetchone()
        return myresult
