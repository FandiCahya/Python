import datetime

def ubah(acara1):
    x = True
    while x :
        try:
            acara1.lihat_jadwal()
            index = int(input("Masukkan nomor acara yang ingin diubah: ")) - 1

            nama_acara_baru = input("Masukkan Nama Acara Baru: ")
            tahun = int(input("Masukkan tahun acara baru (YYYY): "))
            bulan = int(input("Masukkan bulan acara baru (MM): "))
            hari = int(input("Masukkan tanggal acara baru (DD): "))
            jam = int(input("Masukkan jam acara baru (HH): "))
            menit = int(input("Masukkan menit acara baru (MM): "))
            print("="*30)

            waktu_acara_baru = datetime.datetime(tahun, bulan, hari, jam, menit)
            acara1.ubah_acara(index, waktu_acara_baru, nama_acara_baru)
            x=False
            
        except ValueError as e:
            print(f"Terjadi kesalahan: {e}")
            print("Silakan coba lagi.\n")
        except TypeError as e:
            print(f"Terjadi kesalahan: {e}")
            print("Silakan coba lagi.\n")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            print("Silakan coba lagi.\n")
        

