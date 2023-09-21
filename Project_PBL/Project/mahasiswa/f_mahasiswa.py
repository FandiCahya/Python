data_mhs = []
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