import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Regulasi_PKL"
)

mycursor = mydb.cursor()

sql="UPDATE mahasiswa SET nama = %s WHERE nim = %s"
val=("Saiful Yusuf", "2231730003")

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "Data berhasil diupdate.")