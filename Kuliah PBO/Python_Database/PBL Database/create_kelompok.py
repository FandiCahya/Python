import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Regulasi_PKL"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE kelompok (id VARCHAR(20) PRIMARY KEY, nama_kelompok VARCHAR(55))")

mycursor.execute("CREATE TABLE kelompok_mahasiswa (kelompok_id VARCHAR(20), anggota BIGINT(10), FOREIGN KEY (kelompok_id) REFERENCES kelompok(id), FOREIGN KEY (anggota) REFERENCES mahasiswa(nim))")

#-------------------------------------------------------------------------------
