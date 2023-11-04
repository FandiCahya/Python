import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root", 
    password="",
    database="Regulasi_PKL"
)

mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE mahasiswa (nim BIGINT(10) PRIMARY KEY, nama VARCHAR(50), kelas VARCHAR(50))")