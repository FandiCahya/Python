class Mahasiswa:
    def __init__(self, nim, nama, no_hp, alamat):
        self.nim = nim
        self.nama = nama
        self.no_hp = no_hp
        self.alamat = alamat

class KelolaMahasiswa:
    def __init__(self):
        self.data_mhs = []

    # Fungsi untuk melihat data mahasiswa
    def lihat_mahasiswa(self):
        for mhs in self.data_mhs:
            print("=" * 20)
            print("NIM:", mhs.nim)
            print("Nama:", mhs.nama)
            print("No HP:", mhs.no_hp)
            print("Alamat:", mhs.alamat)
            print("=" * 20)
            print("")

    # Fungsi untuk menambah data mahasiswa
    def tambah_mahasiswa(self, nim, nama, no_hp, alamat):
        mahasiswa = Mahasiswa(nim, nama, no_hp, alamat)
        self.data_mhs.append(mahasiswa)

    # Fungsi untuk menghapus data mahasiswa
    def hapus_mahasiswa(self, nim):
        print(self.lihat_mahasiswa())
        for mhs in self.data_mhs:
            if mhs.nim == nim:
                self.data_mhs.remove(mhs)

    # Fungsi untuk mengubah data mahasiswa
    def ubah_mahasiswa(self, nim, nama, no_hp, alamat):
        print(self.lihat_mahasiswa())
        for mhs in self.data_mhs:
            if mhs.nim == nim:
                mhs.nama = nama
                mhs.no_hp = no_hp
                mhs.alamat = alamat
        print(self.lihat_mahasiswa())

    # Fungsi menu untuk mengelola data mahasiswa
    def menu_mahasiswa(self):
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
                self.tambah_mahasiswa(nim, nama, no_hp, alamat)
            elif pilihan == "2":
                self.lihat_mahasiswa()
                nim = input("NIM Mahasiswa yang akan dihapus: ")
                self.hapus_mahasiswa(nim)
            elif pilihan == "3":
                self.lihat_mahasiswa()
                nim = input("NIM Mahasiswa yang akan diubah: ")
                nama = input("Nama Mahasiswa: ")
                no_hp = input("No HP Mahasiswa: ")
                alamat = input("Alamat Mahasiswa: ")
                self.ubah_mahasiswa(nim, nama, no_hp, alamat)
            elif pilihan == "4":
                self.lihat_mahasiswa()
            elif pilihan == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    
    # Fungsi login Mahasiswa
    def login_mahasiswa(self):
        nim = input("Masukkan NIM Mahasiswa: ")
        # Anda dapat mengimplementasikan autentikasi sesuai kebutuhan
        
        # Periksa apakah NIM ada dalam data mahasiswa
        for mhs in self.data_mhs:
            if mhs.nim == nim:
                self.mahasiswa_menu(nim)
                break
        else:
            print("NIM tidak ditemukan.")

# Contoh penggunaan

kelola_mahasiswa = KelolaMahasiswa()
