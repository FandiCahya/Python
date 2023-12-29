import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pbl"
)

mycursor = mydb.cursor()

class Mahasiswa :
    def __init__(self):
        self
    
    def select_data():
        sql = "SElECT * FROM mahasiswa"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        return myresult

    def insert_data(val1,val2,val3,val4,val5):
        sql = "INSERT INTO mahasiswa (nim, nama, kelas, alamat, hp) VALUES (%s,%s,%s,%s,%s)"
        val = (val1,val2, val3, val4,val5)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil ditambahkan")
    
    def delete_data(val1):
        sql = "DELETE FROM mahasiswa WHERE nim = %s"
        value = (val1,)
        mycursor.execute(sql,value)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil dihapus")


    # penting banget ini saja yang dipake

    #mahasiswa
    def update_data_mahasiswa(val1,val2,val3,val4,val5):
        sql = "UPDATE mahasiswa SET nama = %s, kelas=%s, alamat = %s, hp = %s WHERE nim = %s"
        val = (val1,val2, val3, val4,val5)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate")

    def select_data_by_nim(val1):
        sql = "SELECT nim, nama, kelas, alamat, hp FROM mahasiswa WHERE nim = %s"
        val=(val1)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchone()
        return myresult
    
    #dosen
    def update_data_dosen(val1,val2,val3,val4):
        sql = "UPDATE dosen SET nama = %s, alamat = %s, hp = %s WHERE nip = %s"
        val = (val1,val2, val3, val4)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate") 

    def select_data_by_nip(val1):
        sql = "SELECT nip, nama, alamat, hp  FROM dosen WHERE nip = %s"
        val=(val1)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchone()
        return myresult
    
    #instansi
    def update_data_instansi(val1,val2,val3):
        sql = "UPDATE instansi SET nama = %s, alamat = %s WHERE id = %s"
        val = (val1,val2, val3)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate") 

    def select_data_by_id(val1):
        sql = "SELECT id, nama, alamat  FROM instansi WHERE id = %s"
        val=(val1)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchone()
        return myresult 
    
    #user 
    def update_data_user(val1,val2,val3,val4):
        sql = "UPDATE user SET username = %s, password = %s, level = %s  WHERE id = %s"
        val = (val1,val2, val3)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate") 

    def select_data_by_idusr(val1):
        sql = "SELECT id, nama, alamat  FROM instansi WHERE id = %s"
        val=(val1)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchone()
        return myresult 
    

    