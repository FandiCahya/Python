import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Regulasi_PKL"
)

mycursor = mydb.cursor()

sql = "UPDATE kelompok SET nama_kelompok = %s where id = %s"
val = ("Doa IBU", "KLP1",)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Data instansi berhasil diupdate...")


#---------------------------------------------------------------------------------
