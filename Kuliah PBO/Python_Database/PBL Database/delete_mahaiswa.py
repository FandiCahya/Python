import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Regulasi_PKL"
)

mycursor = mydb.cursor()

sql="DELETE FROM mahasiswa WHERE nim =%s"
val=[("2231730086",),("2231730003",)]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "Data berhasil dihapus.")