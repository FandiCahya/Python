import datetime
from jadwalku import acara

# db = []
valid_input = True
while valid_input:
    try:
        n = int(input("Masukkan Jumlah Acara : "))
        if n <= 0:
            raise ValueError("Jumlah acara harus lebih besar dari 0")

        acara1 = acara()
        for i in range(n):
            nama_acara = input(f"Masukkan Nama Acara ke-{i+1} : ")
            tahun = int(input("Masukkan tahun acara (YYYY): "))
            bulan = int(input("Masukkan bulan acara (MM): "))
            hari = int(input("Masukkan tanggal acara (DD): "))
            jam = int(input("Masukkan jam acara (HH): "))
            menit = int(input("Masukkan menit acara (MM): "))
            print("=" * 30)
            waktu_acara = datetime.datetime(tahun, bulan, hari, jam, menit)
            # db.append({"Waktu": waktu_acara, "Acara": nama_acara})
            acara1.tambah_acara(waktu_acara,nama_acara)
        acara1.lihat_jadwal()
        valid_input = False

    except ValueError as e:
        print(f"Terjadi kesalahan: {e}")
        print("Silakan coba lagi.\n")
    except TypeError as e:
        print(f"Terjadi kesalahan: {e}")
        print("Silakan coba lagi.\n")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        print("Silakan coba lagi.\n")