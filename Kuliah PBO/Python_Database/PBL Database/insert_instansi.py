import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Regulasi_PKL"
)
mycursor = mydb.cursor()
sql = "INSERT INTO instansi (id, nama, alamat) VALUES (%s, %s, %s)"
val = [
    ("1", "Viscode", "Mojoroto Kediri"),
    ("2", "KAFA Digital", "Jl. Raden Patah, Kabupaten Kediri"),
    ("3", "Cekotechnology", "Kediri Jawa Timur"),
    ("4", "Hitamedia", "Yogyakarta"),
    ("5", "Qlobot", "Mojoroto Kediri")
    ]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "Data Instansi berhasil ditambahkan...")