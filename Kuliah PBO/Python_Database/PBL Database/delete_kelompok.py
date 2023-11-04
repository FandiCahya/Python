import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Regulasi_PKL"
)

mycursor = mydb.cursor()

sql = "DELETE FROM instansi WHERE id = %s"
value = ("KLP2",)

mycursor.execute(sql, value)

mydb.commit()

print(mycursor.rowcount, "Data instansi berhasil dihapus...")