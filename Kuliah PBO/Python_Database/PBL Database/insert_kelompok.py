import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Regulasi_PKL"
)

mycursor = mydb.cursor()

# Insert values into the kelompok table first
sql_kelompok = "INSERT INTO kelompok (id, nama_kelompok) VALUES (%s, %s)"
val_kelompok = [
    ('KLP1', 'Bujel'),
    ('KLP2', 'Banyakan')
]

mycursor.executemany(sql_kelompok, val_kelompok)
mydb.commit()

# Then insert values into the kelompok_mahasiswa table
sql_kelompok_mahasiswa = "INSERT INTO kelompok_mahasiswa (kelompok_id, anggota) VALUES (%s, %s)"
val_kelompok_mahasiswa = [
    ('KLP1', '2231730001'),
    ('KLP1', '2231730002'),
    ('KLP1', '2231730003')
]

mycursor.executemany(sql_kelompok_mahasiswa, val_kelompok_mahasiswa)
mydb.commit()

print(mycursor.rowcount, "Data berhasil ditambahkan...")

mydb.close()
