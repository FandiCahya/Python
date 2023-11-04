import mysql.connector

# Buat koneksi ke server MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""  # Ganti dengan kata sandi MySQL Anda
)

mycursor = mydb.cursor()

# Buat database regulasi_pkl
mycursor.execute("CREATE DATABASE regulasi_pkl")

# Gunakan database regulasi_pkl
mycursor.execute("USE regulasi_pkl")

# Buat tabel regulasi_pkl
mycursor.execute("CREATE TABLE mahasiswa (id INT AUTO_INCREMENT PRIMARY KEY, nama VARCHAR(255), nim VARCHAR(255), kelas VARCHAR(255))")

# Operasi CRUD

# Create
def tambah_data(nama, nim, kelas):
    sql = "INSERT INTO mahasiswa (nama, nim, kelas) VALUES (%s, %s, %s)"
    val = (nama, nim, kelas)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil ditambahkan.")

# Read
def tampilkan_data():
    mycursor.execute("SELECT * FROM mahasiswa")
    result = mycursor.fetchall()
    for row in result:
        print(row)

# Update
def update_data(nama_baru, nim_baru, kelas_baru, id):
    sql = "UPDATE mahasiswa SET nama = %s, nim = %s, kelas = %s WHERE id = %s"
    val = (nama_baru, nim_baru, kelas_baru, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil diperbarui.")

# Delete
def hapus_data(id):
    sql = "DELETE FROM mahasiswa WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil dihapus.")

# Contoh penggunaan operasi CRUD
tambah_data("Fandi", "123456", "A")
tambah_data("Cahya", "789012", "B")
tampilkan_data()
update_data("Fandi Updated", "123456", "C", 1)
tampilkan_data()
hapus_data(2)
tampilkan_data()

# Tutup koneksi
mydb.close()
