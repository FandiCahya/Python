import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Regulasi_PKL"
)

mycursor = mydb.cursor()

sql = "DELETE FROM instansi "
# value = ("5",)

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "Data instansi berhasil dihapus...")