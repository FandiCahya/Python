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

    def insert_mhs(nama, nim, kelas, alamat, hp):
        try:
            sql = "INSERT INTO mahasiswa (nama, nim, kelas, alamat, hp) VALUES (%s, %s, %s, %s, %s)"
            val = (nama, nim, kelas, alamat, hp)
            cursor.execute(sql, val)
            db_connection.commit()
            print(cursor.rowcount, "Data mahasiswa berhasil ditambahkan...")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def update_mhs(nim, nama_baru, kelas_baru):
        try:
            sql = "UPDATE mahasiswa SET nama = %s, kelas = %s WHERE nim = %s"
            val = (nama_baru, kelas_baru, nim)
            cursor.execute(sql, val)
            db_connection.commit()
            print("Data mahasiswa berhasil diperbarui!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def delete_mhs(self, nim):
        try:
            sql = "DELETE FROM mahasiswa WHERE nim = %s"
            val = (nim,)
            self.cursor.execute(sql, val)
            self.db_connection.commit()
            print("Data mahasiswa berhasil dihapus!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            
    def tampil_mhs(self):
        # os.system("cls" if os.name == "nt" else "clear")
        try:
            sql = "select * from mahasiswa"
            self.cursor.execute(sql)
            myresult = self.cursor.fetchall()
            if len(myresult)>0:
                print("{:<12} {:<20} {:<5}".format('NIM', 'Nama', 'Kelas'))
                print("-" * 40)
                for row in myresult:
                    print("{:<12} {:<20} {:<5}".format(row[0], row[1], row[2]))
            else:
                print("Tidak Tersedia Data Mahasiswa")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def close_connection(self):
        self.cursor.close()
        self.db_connection.close()

