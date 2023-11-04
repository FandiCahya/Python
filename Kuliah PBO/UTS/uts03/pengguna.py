class Pengguna:
    def __init__(self, status):
        self.status = status
        self.data = {}
        self.komentar = {}

    def lihat_informasi(self, nomor_informasi):
        if nomor_informasi in self.data:
            print(self.data[nomor_informasi])
        else:
            print("Informasi tidak ditemukan.")



class Junior(Pengguna):
    def lihat_informasi(self, nomor_informasi):
        super().lihat_informasi(nomor_informasi)
        if nomor_informasi in self.komentar:
            print("Komentar:")
            for komentar in self.komentar[nomor_informasi]:
                print(komentar)

    def tambah_informasi(self, nomor_informasi, informasi):
        self.data[nomor_informasi] = informasi

    def tambah_komentar(self, nomor_informasi, komentar):
        if nomor_informasi not in self.komentar:
            self.komentar[nomor_informasi] = []
        self.komentar[nomor_informasi].append(komentar)

class Senior(Junior):
    def hapus_informasi(self, nomor_informasi):
        try:
            del self.data[nomor_informasi]
            if nomor_informasi in self.komentar:
                del self.komentar[nomor_informasi]
            print(f"Informasi dengan nomor {nomor_informasi} telah dihapus.")
        except KeyError:
            print(f"Informasi dengan nomor {nomor_informasi} tidak ditemukan.")

    def lihat_informasi2(self):
        print("Informasi:")
        for nomor, info in self.data.items():
            print(f"{nomor}: {info}")
        
        print("\nKomentar:")
        for nomor, komen in self.komentar.items():
            print(f"{nomor}: {komen}")

    def menu(self):
        while True:
            print("\nMenu Senior:")
            print("1. Lihat Informasi")
            print("2. Tambah Informasi")
            print("3. Tambah Komentar")
            print("4. Hapus Informasi")
            print("5. Keluar")
            pilihan = input("Pilih menu (1/2/3/4/5): ")

            if pilihan == "1":
                nomor_informasi = int(input("Masukkan nomor informasi: "))
                self.lihat_informasi(nomor_informasi)
            elif pilihan == "2":
                nomor_informasi = int(input("Masukkan nomor informasi: "))
                informasi = input("Masukkan informasi: ")
                self.tambah_informasi(nomor_informasi, informasi)
            elif pilihan == "3":
                nomor_informasi = int(input("Masukkan nomor informasi: "))
                komentar = input("Masukkan komentar: ")
                self.tambah_komentar(nomor_informasi, komentar)
            elif pilihan == "4":
                nomor_informasi = int(input("Masukkan nomor informasi yang akan dihapus: "))
                self.hapus_informasi(nomor_informasi)
            elif pilihan == "5":
                break
            elif pilihan == "6":
                self.lihat_informasi2()
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")