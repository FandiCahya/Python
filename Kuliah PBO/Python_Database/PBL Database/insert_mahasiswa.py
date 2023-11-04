import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Regulasi_PKL"
)

mycursor = mydb.cursor()

sql="INSERT INTO mahasiswa (nim, nama, kelas) VALUES (%s, %s, %s)"
val=[
    ('2231730001', 'fandi', '2D'),
    ('2231730002', 'candra', '2D'),
    ('2231730003', 'saipul', '2D'),
    ('2231730004', 'putri', '2D'),
    ('2231730005', 'delia', '2D'),
    ('2231730006', 'alvin', '2D')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "Data berhasil ditambahkan...")