import mysql.connector

db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbl"
)
cursor = db_connection.cursor()

class Mahasiswa:

    def __init__(self):
        self

    def tampil (self):
        sql = "select * from mahasiswa"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        return myresult
    
    def cari_data (nim):
        sql = "SELECT nim, nama, kelas, alamat, hp, dosen FROM mahasiswa where nim = %s "
        val = (nim,)
        cursor.execute(sql,val)
        myresult = cursor.fetchone()
        return myresult
    
    def select_data():
        sql = "SELECT * FROM mahasiswa"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)

    def insert_mhs(nim, nama, kelas, alamat, hp,dosen):
        try:
            sql = "INSERT INTO mahasiswa (nama, nim, kelas, alamat, hp, dosen) VALUES (%s, %s, %s, %s, %s)"
            val = (nim, nama, kelas, alamat, hp,dosen)
            cursor.execute(sql, val)
            db_connection.commit()
            print(cursor.rowcount, "Data mahasiswa berhasil ditambahkan...")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def update_mhs(val1,val2,val3,val4,val5,val6):
        try:
            sql = "UPDATE mahasiswa SET nama = %s, kelas = %s, alamat = %s, hp = %s, dosen = %s WHERE nim = %s"
            val = (val1,val2,val3,val4,val5,val6)
            cursor.execute(sql, val)
            db_connection.commit()
            print(cursor.rowcount, "Data mahasiswa berhasil diperbarui...")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def delete_mhs(nim):
        try:
            sql = "DELETE FROM mahasiswa WHERE nim = %s"
            val = (nim,)
            cursor.execute(sql, val)
            db_connection.commit()
            print(cursor.rowcount, "Data mahasiswa berhasil dihapus...")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            
    # def tampil_mhs(self):
    #     # os.system("cls" if os.name == "nt" else "clear")
    #     try:
    #         sql = "select * from mahasiswa"
    #         self.cursor.execute(sql)
    #         myresult = self.cursor.fetchall()
    #         if len(myresult)>0:
    #             print("{:<12} {:<20} {:<5}".format('NIM', 'Nama', 'Kelas'))
    #             print("-" * 40)
    #             for row in myresult:
    #                 print("{:<12} {:<20} {:<5}".format(row[0], row[1], row[2]))
    #         else:
    #             print("Tidak Tersedia Data Mahasiswa")
    #     except mysql.connector.Error as err:
    #         print(f"Error: {err}")

    # def close_connection(self):
    #     self.cursor.close()
    #     self.db_connection.close()

