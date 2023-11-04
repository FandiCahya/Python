import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Regulasi_PKL"
)

mycursor = mydb.cursor()

sql = "UPDATE instansi SET alamat = %s WHERE id = %s"
val = ("Lumajang", "4",)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Data instansi berhasil diupdate...")


#---------------------------------------------------------------------------------
