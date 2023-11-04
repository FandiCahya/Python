import datetime

def tambah(acara1):
    x = True
    while x :
        try:
            n = int(input("Masukkan jumlah acara yang ingin ditambahkan: "))
            if n <= 0:
                raise ValueError("Jumlah acara harus lebih besar dari 0")

            for _ in range(n):
                nama_acara = input("Masukkan Nama Acara: ")
                tahun = int(input("Masukkan tahun acara (YYYY): "))
                bulan = int(input("Masukkan bulan acara (MM): "))
                hari = int(input("Masukkan tanggal acara (DD): "))
                jam = int(input("Masukkan jam acara (HH): "))
                menit = int(input("Masukkan menit acara (MM): "))
                print("="*30)

                waktu_acara = datetime.datetime(tahun, bulan, hari, jam, menit)
                id_acara = len(acara1.list_jadwal) + 1
                acara1.tambah_acara(waktu_acara, nama_acara, id_acara)

            acara1.lihat_jadwal()
            x = False

        except ValueError as e:
            print(f"Terjadi kesalahan: {e}")
            print("Silakan coba lagi.\n")
        except TypeError as e:
            print(f"Terjadi kesalahan: {e}")
            print("Silakan coba lagi.\n")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            print("Silakan coba lagi.\n")

