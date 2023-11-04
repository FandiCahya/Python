import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="",
    database = "Regulasi_PKL"
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM mahasiswa ")

# mycursor.execute("SELECT * FROM instansi ")

# mycursor.execute("SELECT * FROM kelompok ")

# mycursor.execute("SELECT * FROM kelompok_mahasiswa ")


mycursor.execute("SELECT kelompok.id, kelompok.nama_kelompok, mahasiswa.nim, mahasiswa.nama FROM kelompok JOIN kelompok_mahasiswa ON kelompok.id = kelompok_mahasiswa.kelompok_id JOIN mahasiswa ON kelompok_mahasiswa.anggota = mahasiswa.nim")
print("\nData Kelompok and Kelompok_Mahasiswa:")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)