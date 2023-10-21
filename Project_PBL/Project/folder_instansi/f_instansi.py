
class Instansi:
    def __init__(self, id_instansi, nama_instansi, alamat_instansi):
        self.id_instansi = id_instansi
        self.nama_instansi = nama_instansi
        self.alamat_instansi = alamat_instansi

class KelolaInstansi():
    def __init__(self):
        self.data_instansi = []

    # Fungsi untuk melihat data instansi
    def lihat_instansi(self):
        for instansi in self.data_instansi:
            print("=" * 20)
            print("ID Instansi:", instansi.id_instansi)
            print("Nama Instansi:", instansi.nama_instansi)
            print("Alamat Instansi:", instansi.alamat_instansi)
            print("=" * 20)
            print("")

    # Fungsi untuk menambah data instansi
    def tambah_instansi(self, id_instansi, nama_instansi, alamat_instansi):
        instansi = Instansi(id_instansi, nama_instansi, alamat_instansi)
        self.data_instansi.append(instansi)

    # Fungsi untuk menghapus data instansi
    def hapus_instansi(self, id_instansi):
        print(self.lihat_instansi())
        for instansi in self.data_instansi:
            if instansi.id_instansi == id_instansi:
                self.data_instansi.remove(instansi)

    # Fungsi untuk mengubah data instansi
    def ubah_instansi(self, id_instansi, nama_instansi, alamat_instansi):
        for instansi in self.data_instansi:
            if instansi.id_instansi == id_instansi:
                instansi.nama_instansi = nama_instansi
                instansi.alamat_instansi = alamat_instansi

    # Fungsi menu untuk mengelola data instansi
    def menu_instansi(self):
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
                self.tambah_instansi(id_instansi, nama_instansi, alamat_instansi)
            elif pilihan == "2":
                self.lihat_instansi()
                id_instansi = input("ID Instansi yang akan dihapus: ")
                self.hapus_instansi(id_instansi)
            elif pilihan == "3":
                self.lihat_instansi()
                id_instansi = input("ID Instansi yang akan diubah: ")
                nama_instansi = input("Nama Instansi: ")
                alamat_instansi = input("Alamat Instansi: ")
                self.ubah_instansi(id_instansi, nama_instansi, alamat_instansi)
            elif pilihan == "4":
                self.lihat_instansi()
            elif pilihan == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
