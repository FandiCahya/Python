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
        sql = "SELECT nim, nama, kelas, alamat, hp FROM mahasiswa where nim = %s "
        val = (nim,)
        cursor.execute(sql,val)
        myresult = cursor.fetchone()
        return myresult
    
    def select_data():
        sql = "SELECT nama FROM mahasiswa"
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

    # def insert_mhs(nim, nama, kelas, alamat, hp):
    #     sql = "INSERT INTO mahasiswa (nim, nama, kelas, alamat, hp) VALUES (%s, %s, %s, %s, %s"
    #     val = (nim, nama, kelas, alamat, hp)
    #     cursor.execute(sql, val)
    #     db_connection.commit()
    #     print(cursor.rowcount, "Data mahasiswa berhasil ditambahkan...")
        
    def insert_mhs(val1, val2, val3, val4, val5):
        sql = "INSERT INTO mahasiswa (nim, nama, kelas, alamat, hp) VALUES (%s, %s, %s, %s, %s)"
        val = (val1, val2, val3, val4, val5)
        cursor.execute(sql, val)
        db_connection.commit()
        print(cursor.rowcount, "Data mahasiswa berhasil ditambahkan...")

    def update_data_mahasiswa(val1,val2,val3,val4,val5):
        sql = "UPDATE mahasiswa SET nama = %s, kelas=%s, alamat = %s, hp = %s WHERE nim = %s"
        val = (val1,val2, val3, val4,val5)
        cursor.execute(sql,val)
        db_connection.commit()
        print(cursor.rowcount, "Data berhasil diupdate")
            
    def select_data_by_nim(val1):
        sql = "SELECT nim, nama, kelas, alamat, hp FROM mahasiswa WHERE nim = %s"
        val=(val1)
        cursor.execute(sql,val)
        myresult=cursor.fetchone()
        return myresult

    def delete_mhs(nim):
        try:
            sql = "DELETE FROM mahasiswa WHERE nim = %s"
            val = (nim,)
            cursor.execute(sql, val)
            db_connection.commit()
            print(cursor.rowcount, "Data mahasiswa berhasil dihapus...")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            
