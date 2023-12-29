import mysql.connector

db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbl"
)
cursor = db_connection.cursor()

class Dosen:


    def __init__(self):
        self
        
    def tampil (self):
        sql = "select * from dosen"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        return myresult
    
    def cari_data (nip):
        sql = "SELECT nip, nama, alamat FROM dosen where nip = %s "
        val = (nip,)
        cursor.execute(sql,val)
        myresult = cursor.fetchone()
        return myresult
    
    def select_data():
        sql = "SELECT * FROM dosen"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)

    def insert_ins(nip, nama, alamat):
        try:
            sql = "INSERT INTO dosen (nip, nama, alamat) VALUES (%s, %s, %s)"
            val = (nip, nama, alamat)
            cursor.execute(sql, val)
            db_connection.commit()
            print("Data instansi berhasil ditambahkan!")
            print(cursor.rowcount, "Data Instansi berhasil ditambahkan...")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def update_ins(nip, nama_baru, alamat_baru):
        try:
            sql = "UPDATE dosen SET nama = %s, alamat = %s WHERE nip = %s"
            val = (nama_baru, alamat_baru, nip)
            cursor.execute(sql, val)
            db_connection.commit()
            print(cursor.rowcount, "Data Instansi berhasil diperbarui...")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def delete_ins(nip):
        try:
            sql = "DELETE FROM dosen WHERE nip = %s"
            val = (nip,)
            cursor.execute(sql, val)
            db_connection.commit()
            print(cursor.rowcount, "Data Instansi berhasil dihapus...")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            
    # def tampil_ins(self):
    #     os.system("cls" if os.name == "nt" else "clear")
    #     try:
    #         sql = "select * from instansi"
    #         self.cursor.execute(sql)
    #         myresult = self.cursor.fetchall()
    #         if len(myresult)>0:
    #             print("{:<5} {:<20} {:<50}".format('nip', 'Nama', 'Alamat'))
    #             print("-" * 50)
    #             for row in myresult:
    #                 print("{:<5} {:<20} {:<50}".format(row[0], row[1], row[2]))
    #         else:
    #             print("Tnipak Tersedia Data Mahasiswa")
    #     except mysql.connector.Error as err:
    #         print(f"Error: {err}")

    # def close_connection(self):
    #     self.cursor.close()
    #     self.db_connection.close()

