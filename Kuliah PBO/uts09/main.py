from amkp.kesehatan import sehat
from amkp.pengguna import orang


def main():
    sehat1 = sehat()
    while True:
        try:
            print("Selamat datang di Program Pengecek Kesehatan")
            print("Menu:")
            print("1. Masukkan Nama & Umur")
            print("2. Masukkan Parameter Kesehatan")
            print("3. Cek Kesehatan")
            print("4. Keluar")
            pilihan = input("Pilih menu : ")

            if pilihan == "1":
                orang1 = orang()
                nama, umur = orang1.daftar()
                print(orang1.cek_kondisi_umum())
                print()
                sehat1 = sehat(nama, umur)
                
            elif pilihan == "2":
                sehat1.input_data_kesehatan()
                print()
                
            elif pilihan == "3":
                print(sehat1.cek_kondisi_umum())
                print("------------------------------------------")
                hasil_pengecekan = sehat1.cek_kesehatan_umum()
                if hasil_pengecekan:
                    print("Diagnosis :")
                    for h in hasil_pengecekan:
                        print("-"+h)
                print("------------------------------------------")
                saran = sehat1.berikan_saran()
                if saran:
                    print("Saran-saran :")
                    for s in saran:
                        print("-"+s)
                print()

            elif pilihan == "4":
                print("Terima kasih. Sampai jumpa lagi!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang benar")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            print("Silakan coba lagi.\n")

if __name__ == "__main__":
    main()
