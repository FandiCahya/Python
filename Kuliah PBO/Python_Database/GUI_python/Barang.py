import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my_oop_database"
)
mycursor = mydb.cursor()

class Barang:
    def __init__(self):
        self
        
    def nilai(self):
        sql = "SELECT * FROM Barang"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    
    def select_data_by_id(id):
        sql = "SELECT id, nama, stok, harga, kategori FROM barang WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        return myresult

    def select_data():
        sql = "SELECT * FROM barang"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
            
    def insert_data(val1,val2,val3,val4,val5):
        sql = "INSERT INTO barang (id, nama, stok, harga, kategori) VALUES (%s, %s, %s, %s, %s)"
        val = (val1,val2,val3,val4,val5)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil ditambahkan...")
        
    def update_data(val1,val2,val3,val4,val5):
        sql = "UPDATE barang SET nama = %s, stok = %s, harga = %s, kategori = %s WHERE id = %s"
        val = (val1,val2,val3,val4,val5)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate...")
        
    def delete_data(val1):
        sql = "DELETE FROM barang WHERE id = %s"
        value = (val1, )
        mycursor.execute(sql, value)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil dihapus")