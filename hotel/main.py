from hotel import Hotel, KamarSingle, KamarDouble

def pemesanan_hotel():
    hotel = Hotel("Hotel Hargo", 3)  # Membuat objek hotel
    print(hotel.informasi())  # Menampilkan informasi tentang hotel

    try:
        print("\nPilih tipe kamar:")  # Menampilkan pilihan tipe kamar
        print("1. Kamar Single")
        print("2. Kamar Double")
        tipe_kamar = int(input("Pilihan Anda: "))  # Meminta pilihan tipe kamar dari pengguna

        if tipe_kamar == 1:
            kamar = KamarSingle("101")  # Membuat objek kamar single
        elif tipe_kamar == 2:
            kamar = KamarDouble("201")  # Membuat objek kamar double
        else:
            raise ValueError("Pilihan tipe kamar tidak valid.")  # Raise exception jika pilihan tipe kamar tidak valid

        jumlah_malam = int(input("Jumlah malam menginap: "))  # Meminta jumlah malam menginap
        jumlah_tamu = int(input("Jumlah tamu: "))  # Meminta jumlah tamu

        total_harga = kamar.pesan_kamar(jumlah_malam, jumlah_tamu)  # Pesan kamar dan hitung total harga
        print("\nPesanan Berhasil!")  # Menampilkan pesan pesanan berhasil
        print(kamar.informasi())  # Menampilkan informasi kamar
        print(f"Total Harga: {total_harga}")  # Menampilkan total harga

    except ValueError as e:
        print(f"Terjadi kesalahan: {e}")  # Menampilkan pesan kesalahan jika terjadi exception

if __name__ == "__main__":
    pemesanan_hotel()  # Memanggil fungsi pemesanan_hotel() saat file ini dijalankan
