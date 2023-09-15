import os

if __name__ == "__main__":
    sistem_operasi = os.name
# Inisialisasi data
data_mhs = []
data_instansi = []
data_kelompok = []

# Fungsi untuk melihat data mahasiswa
def lihat_mahasiswa():
    for mhs in data_mhs:
        print("="*20)
        print("NIM:", mhs["nim"])
        print("Nama:", mhs["nama"])
        print("No HP:", mhs["no_hp"])
        print("Alamat:", mhs["alamat"])
        print("="*20)
        print("")

# Fungsi untuk menambah data mahasiswa
def tambah_mahasiswa(nim, nama, no_hp, alamat):
    data_mhs.append({
        "nim": nim, 
        "nama": nama, 
        "no_hp": no_hp, 
        "alamat": alamat
        })

# Fungsi untuk menghapus data mahasiswa
def hapus_mahasiswa(nim):
    print(lihat_mahasiswa())
    for mhs in data_mhs:
        if mhs["nim"] == nim:
            data_mhs.remove(mhs)

# Fungsi untuk mengubah data mahasiswa
def ubah_mahasiswa(nim, nama, no_hp, alamat):
    print(lihat_mahasiswa())
    for mhs in data_mhs:
        if mhs["nim"] == nim :
            mhs["nama"] = nama
            mhs["no_hp"] = no_hp
            mhs["alamat"] = alamat
    print(lihat_mahasiswa())
            
# Fungsi untuk melihat data instansi
def lihat_instansi():
    for instansi in data_instansi:
        print("="*20)
        print("ID Instansi:", instansi["id_instansi"])
        print("Nama Instansi:", instansi["nama_instansi"])
        print("Alamat Instansi:", instansi["alamat_instansi"])
        print("="*20)
        print("")

# Fungsi untuk menambah data instansi
def tambah_instansi(id_instansi, nama_instansi, alamat_instansi):
    data_instansi.append({"id_instansi": id_instansi, "nama_instansi": nama_instansi, "alamat_instansi": alamat_instansi})

# Fungsi untuk menghapus data instansi
def hapus_instansi(id_instansi):
    print(lihat_instansi())
    for instansi in data_instansi:
        if instansi["id_instansi"] == id_instansi:
            data_instansi.remove(instansi)

# Fungsi untuk mengubah data instansi
def ubah_instansi(id_instansi, nama_instansi, alamat_instansi):
    for instansi in data_instansi:
        if instansi["id_instansi"] == id_instansi:
            instansi["nama_instansi"] = nama_instansi
            instansi["alamat_instansi"] = alamat_instansi


# Fungsi untuk menambah data kelompok
def tambah_kelompok(id_kelompok, nama_instansi, lama_pkl, list_nim):
    # Temukan instansi berdasarkan id_instansi
    instansi = None
    for data in data_instansi:
        if data["nama_instansi"] == nama_instansi:
            instansi = data
            break

    if instansi is None:
        print("Instansi dengan nama tersebut tidak ditemukan.")
        return

    # Temukan mahasiswa berdasarkan NIM
    mahasiswas_kelompok = []
    for nim in list_nim:
        found = False
        for data in data_mhs:
            if data["nim"] == nim:
                mahasiswas_kelompok.append(data)
                found = True
                break
        if not found:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    data_kelompok.append({
        "id_kelompok": id_kelompok,
        "nama_instansi": instansi["nama_instansi"],
        "lama_pkl": lama_pkl,
        "list_nim": [mhs["nim"] for mhs in mahasiswas_kelompok]
    })

    print("Data kelompok berhasil ditambahkan.")


# Fungsi untuk melihat data kelompok
def lihat_kelompok():
    for kelompok in data_kelompok:
        print("="*20)
        print("ID Kelompok:", kelompok["id_kelompok"])
        print("Nama Instansi:", kelompok["nama_instansi"])
        print("Lama PKL:", kelompok["lama_pkl"]," Bulan")
        print("NIM dalam Kelompok:", kelompok["list_nim"])
        print("="*20)
        print("")
    

# Fungsi utama untuk Admin
def admin_menu():
    while True:
        match sistem_operasi:
            case "nt": os.system("cls")
        print("===== Menu Admin =====")
        print("1. Kelola Data Mahasiswa")
        print("2. Kelola Data Instansi")
        print("3. Kelola Data Kelompok")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_mahasiswa()
        elif pilihan == "2":
            menu_instansi()
        elif pilihan == "3":
            menu_kelompok()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        

# Fungsi menu untuk mengelola data mahasiswa
def menu_mahasiswa():
    while True:
        print("\n===== Menu Kelola Data Mahasiswa =====")
        print("1. Tambah Mahasiswa")
        print("2. Hapus Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Lihat Mahasiswa")
        print("5. Kembali ke Menu Admin")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim = input("NIM Mahasiswa: ")
            nama = input("Nama Mahasiswa: ")
            no_hp = input("No HP Mahasiswa: ")
            alamat = input("Alamat Mahasiswa: ")
            tambah_mahasiswa(nim, nama, no_hp, alamat)
        elif pilihan == "2":
            lihat_mahasiswa()
            nim = input("NIM Mahasiswa yang akan dihapus: ")
            hapus_mahasiswa(nim)
        elif pilihan == "3":
            lihat_mahasiswa()
            nim = input("NIM Mahasiswa yang akan diubah: ")
            nama = input("Nama Mahasiswa: ")
            no_hp = input("No HP Mahasiswa: ")
            alamat = input("Alamat Mahasiswa: ")
            ubah_mahasiswa(nim, nama, no_hp, alamat)
        elif pilihan == "4":
            lihat_mahasiswa()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi menu untuk mengelola data instansi
def menu_instansi():
    while True:
        print("\n===== Menu Kelola Data Instansi =====")
        print("1. Tambah Instansi")
        print("2. Hapus Instansi")
        print("3. Ubah Instansi")
        print("4. Lihat Instansi")
        print("5. Kembali ke Menu Admin")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            id_instansi = input("ID Instansi: ")
            nama_instansi = input("Nama Instansi: ")
            alamat_instansi = input("Alamat Instansi: ")
            tambah_instansi(id_instansi, nama_instansi, alamat_instansi)
        elif pilihan == "2":
            lihat_instansi()
            id_instansi = input("ID Instansi yang akan dihapus: ")
            hapus_instansi(id_instansi)
        elif pilihan == "3":
            lihat_instansi()
            id_instansi = input("ID Instansi yang akan diubah: ")
            nama_instansi = input("Nama Instansi: ")
            alamat_instansi = input("Alamat Instansi: ")
            ubah_instansi(id_instansi, nama_instansi, alamat_instansi)
        elif pilihan == "4":
            lihat_instansi()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi menu untuk mengelola data kelompok
def menu_kelompok():
    while True:
        print("\n===== Menu Kelola Data Kelompok =====")
        print("1. Tambah Kelompok")
        print("2. Lihat Kelompok")
        print("3. Kembali ke Menu Admin")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_mahasiswa()
            lihat_instansi()
            id_kelompok = input("ID Kelompok: ")
            nama_instansi = input("Nama Instansi : ")
            lama_pkl = input("Lama PKL: ")
            list_nim = input("NIM dalam Kelompok (pisahkan dengan koma): ").split(",")
            tambah_kelompok(id_kelompok, nama_instansi,lama_pkl, list_nim)
        elif pilihan == "2":
            lihat_kelompok()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi utama untuk Mahasiswa
def mahasiswa_menu(nim):
    while True:
        print("\n===== Menu Mahasiswa =====")
        print("1. Lihat Mahasiswa")
        print("2. Lihat Instansi")
        print("3. Lihat Kelompok")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_mahasiswa()
        elif pilihan == "2":
            lihat_instansi()
        elif pilihan == "3":
            lihat_kelompok()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Fungsi login Admin
def login_admin():
    username = input("Masukkan username Admin: ")
    password = input("Masukkan password Admin: ")  # Anda dapat mengimplementasikan autentikasi sesuai kebutuhan

    if username == "admin" and password == "admin":  # Gantilah dengan autentikasi yang sesuai
        admin_menu()
    else:
        print("Login gagal. Coba lagi.")

# Fungsi login Mahasiswa
def login_mahasiswa():
    nim = input("Masukkan NIM Mahasiswa: ")
    # Anda dapat mengimplementasikan autentikasi sesuai kebutuhan
    
    # Periksa apakah NIM ada dalam data mahasiswa
    for mhs in data_mhs:
        if mhs["nim"] == nim:
            mahasiswa_menu(nim)
            break
    else:
        print("NIM tidak ditemukan.")

# Program Utama
while True:
    match sistem_operasi:
        case "nt": os.system("cls")
    print("===== Sistem Informasi PKL =====")
    print("1. Login Admin")
    print("2. Login Mahasiswa")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        login_admin()
    elif pilihan == "2":
        login_mahasiswa()
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
