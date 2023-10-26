
from crud.tambah_acara import tambah
from crud.ubah_acara import ubah
from crud.hapus_acara import hapus
from module.Jadwal import acara


acara1 = acara()

x = True
while x:
    try:
        print("1. Tambah Acara ")
        print("2. Ubah Acara ")
        print("3. Hapus Acara ")
        print("4. Lihat Acara")
        print("5. Keluar ")
        inp = int(input("Masukkan Pilihan Anda : " ))
        
        if inp == 1 :
            tambah(acara1)
        elif inp == 2 :
            ubah(acara1)
        elif inp == 3 :
            hapus(acara1)
        elif inp == 4 :
            acara1.lihat_jadwal()
        elif inp == 5:
            x = False
        else:
            print("Inputan Tidak ada")
    except ValueError as e:
        print(f"Terjadi kesalahan: {e}")
        print("Silakan coba lagi.\n")
    except TypeError as e:
        print(f"Terjadi kesalahan: {e}")
        print("Silakan coba lagi.\n")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        print("Silakan coba lagi.\n")
