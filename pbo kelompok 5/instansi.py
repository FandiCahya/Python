import mysql.connector

db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbl"
)
cursor = db_connection.cursor()

class Instansi:


    def __init__(self):
        self
        
    def tampil (self):
        sql = "select * from instansi"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        return myresult
    
    def cari_data (id):
        sql = "SELECT id, nama, alamat FROM instansi where id = %s "
        val = (id,)
        cursor.execute(sql,val)
        myresult = cursor.fetchone()
        return myresult
    
    def select_data():
        sql = "SELECT nama FROM instansi"
        cursor.execute(sql)
        myresult= cursor.fetchall()
        data=[]
        for x in myresult:
            data.append(str(x).replace("(","")
                        .replace("'","")
                        .replace(",","")
                        .replace(")","")) #hapus karakter object
            print(x)
        return data

    def insert_ins(id, nama, alamat):
        try:
            sql = "INSERT INTO instansi (id, nama, alamat) VALUES (%s, %s, %s)"
            val = (id, nama, alamat)
            cursor.execute(sql, val)
            db_connection.commit()
            print("Data instansi berhasil ditambahkan!")
            print(cursor.rowcount, "Data Instansi berhasil ditambahkan...")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    # def update_ins(id, nama_baru, alamat_baru):
    #     try:
    #         sql = "UPDATE instansi SET nama = %s, alamat = %s WHERE id = %s"
    #         val = (nama_baru, alamat_baru, id)
    #         cursor.execute(sql, val)
    #         db_connection.commit()
    #         print(cursor.rowcount, "Data Instansi berhasil diperbarui...")

    #     except mysql.connector.Error as err:
    #         print(f"Error: {err}")
            
    def update_data_instansi(val1,val2,val3):
        sql = "UPDATE instansi SET nama = %s, alamat = %s WHERE id = %s"
        val = (val1,val2, val3)
        cursor.execute(sql,val)
        db_connection.commit()
        print(cursor.rowcount, "Data berhasil diupdate")

    def select_data_by_id(val1):
        sql = "SELECT id, nama, alamat FROM instansi WHERE id = %s"
        val=(val1)
        cursor.execute(sql,val)
        myresult=cursor.fetchone()
        return myresult

    def delete_ins(id):
        try:
            sql = "DELETE FROM instansi WHERE id = %s"
            val = (id,)
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
    #             print("{:<5} {:<20} {:<50}".format('id', 'Nama', 'Alamat'))
    #             print("-" * 50)
    #             for row in myresult:
    #                 print("{:<5} {:<20} {:<50}".format(row[0], row[1], row[2]))
    #         else:
    #             print("Tidak Tersedia Data Mahasiswa")
    #     except mysql.connector.Error as err:
    #         print(f"Error: {err}")

    # def close_connection(self):
    #     self.cursor.close()
    #     self.db_connection.close()

