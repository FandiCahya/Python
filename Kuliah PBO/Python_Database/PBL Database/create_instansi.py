import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Regulasi_PKL"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE instansi (id VARCHAR(20) PRIMARY KEY, nama VARCHAR(55), alamat VARCHAR(55))")

#-------------------------------------------------------------------------------
