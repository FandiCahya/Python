import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my_oop_database"
)
mycursor = mydb.cursor()

class pegawai :
    def __init__(self):
        self
    
    def nilai (self):
        sql = "select * from pegawai"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult

    def cari_data (nip):
        sql = "SELECT nip, nama, hp, jabatan, alamat, departemen FROM pegawai where nip = %s "
        val = (nip,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchone()
        return myresult

    def select_data():
        sql = "SELECT * FROM prgawai"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def insert_data(val1, val2, val3, val4, val5, val6, val7):
        sql = "INSERT INTO pegawai (nip, nama, hp, jabatan, alamat, departemen, gambar) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (val1, val2, val3, val4, val5, val6, val7)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil ditambahkan...")

        
    def update_data(val1,val2,val3,val4,val5,val6,val7):
        sql = "UPDATE pegawai SET nama = %s, hp = %s, jabatan = %s, alamat = %s, departemen = %s, gambar = %s WHERE nip = %s"
        val = (val1,val2,val3,val4,val5,val6,val7)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate...")
        
    def delete_data(val1):
        sql = "DELETE FROM pegawai WHERE nip = %s"
        value = (val1, )
        mycursor.execute(sql, value)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil dihapus")