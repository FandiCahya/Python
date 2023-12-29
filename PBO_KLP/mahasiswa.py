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
    
    def select_data_ku():
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
    
    def select_data():
        sql = "SELECT * FROM mahasiswa"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)

    def insert_mhs(val1, val2, val3, val4, val5, val6, val7):
        sql = "INSERT INTO mahasiswa (nim, nama, kelas, alamat, hp, dosen,instansi) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (val1, val2, val3, val4, val5, val6, val7)
        cursor.execute(sql, val)
        db_connection.commit()
        print(cursor.rowcount, "Data mahasiswa berhasil ditambahkan...")

    def update_data_mahasiswa(val1,val2,val3,val4,val5,val6,val7):
        sql = "UPDATE mahasiswa SET nama = %s, kelas=%s, alamat = %s, hp = %s, dosen=%s, instansi=%s WHERE nim = %s"
        val = (val1,val2, val3, val4,val5,val6,val7)
        cursor.execute(sql,val)
        db_connection.commit()
        print(cursor.rowcount, "Data berhasil diupdate")
            
    def select_data_by_nim(val1):
        sql = "SELECT nim, nama, kelas, alamat, hp, dosen, instansi FROM mahasiswa WHERE nim = %s"
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
            
