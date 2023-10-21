from sys import path
path.append('E:\Python\Project_PBL\Project')

from folder_instansi.f_instansi import KelolaInstansi
from mahasiswa.f_mahasiswa1 import KelolaMahasiswa

ki = KelolaInstansi()
lm = KelolaMahasiswa()

class Kelompok():
    def __init__(self):
        self.data_kelompok = []

    def tambah_kelompok(self, id_kelompok, instansi, lama_pkl, list_nim):
        instansi_data = ki.cari_instansi(instansi.data_instansi())

        if not instansi_data:
            print("Instansi dengan nama tersebut tidak ditemukan.")
            return

        mahasiswas_kelompok = []
        for nim in list_nim:
            mahasiswa_data = lm.cari_mahasiswa(nim)
            if mahasiswa_data:
                mahasiswas_kelompok.append(mahasiswa_data)
            else:
                print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

        self.data_kelompok.append({
            "id_kelompok": id_kelompok,
            "nama_instansi": instansi_data["nama_instansi"],
            "lama_pkl": lama_pkl,
            "list_nim": [mhs["nim"] for mhs in mahasiswas_kelompok]
        })

        print("Data kelompok berhasil ditambahkan.")


    def lihat_kelompok(self):
        for kelompok in self.data_kelompok:
            print("=" * 20)
            print("ID Kelompok:", kelompok["id_kelompok"])
            print("Nama Instansi:", kelompok["nama_instansi"])
            print("Lama PKL:", kelompok["lama_pkl"], " Bulan")
            print("NIM dalam Kelompok:", kelompok["list_nim"])
            print("=" * 20)
            print("")

class MenuKelompok:
    # def __init__(self, mahasiswa, instansi, kelompok):
    #     self.mahasiswa = mahasiswa
    #     self.instansi = instansi
    #     self.kelompok = kelompok

    def menu_kelompok(self):
        while True:
            print("\n===== Menu Kelola Data Kelompok =====")
            print("1. Tambah Kelompok")
            print("2. Lihat Kelompok")
            print("3. Kembali ke Menu Admin")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                # self.mahasiswa.lihat_mahasiswa()
                # self.instansi.lihat_instansi()
                id_kelompok = input("ID Kelompok: ")
                instansi_nama = input("Nama Instansi : ")
                lama_pkl = input("Lama PKL: ")
                list_nim = input("NIM dalam Kelompok (pisahkan dengan koma): ").split(",")
                self.kelompok.tambah_kelompok(id_kelompok, self.instansi, lama_pkl, list_nim)
            elif pilihan == "2":
                self.kelompok.lihat_kelompok()
            elif pilihan == "3":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

# if __name__ == "__main__":
#     mahasiswa = KelolaMahasiswa()
#     instansi = KelolaInstansi()
#     kelompok = Kelompok()

#     menu_kelompok = MenuKelompok(mahasiswa, instansi, kelompok)

#     while True:
#         print("===== Menu Admin =====")
#         print("1. Kelola Data Mahasiswa")
#         print("2. Kelola Data Instansi")
#         print("3. Kelola Data Kelompok")
#         print("4. Keluar")
#         pilihan = input("Pilih menu: ")

#         if pilihan == "1":
#             mahasiswa.menu_mahasiswa()
#         elif pilihan == "2":
#             instansi.menu_instansi()
#         elif pilihan == "3":
#             menu_kelompok.menu_kelompok()
#         elif pilihan == "4":
#             break
#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.")
