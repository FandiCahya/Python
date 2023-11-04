def hapus(acara1):
    try: 
        acara1.lihat_jadwal()
        index = int(input("Masukkan nomor acara yang ingin dihapus: ")) - 1

        acara1.hapus_acara(index)
        
    except ValueError as e:
        print(f"Terjadi kesalahan: {e}")
        print("Silakan coba lagi.\n")
    except TypeError as e:
        print(f"Terjadi kesalahan: {e}")
        print("Silakan coba lagi.\n")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        print("Silakan coba lagi.\n")


