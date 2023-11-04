import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my_oop_database"
)

mycursor = mydb.cursor()

sql = "INSERT INTO user (nama, username, password, level) VALUES (%s, %s, %s, %s)"
val = [
    ("Bella", "bella", "bella000", "Kasir"),
    ("Chacha", "chacha", "chacha000", "Kasir")
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "Data berhasil ditambahkan....")