class Hotel:
    def __init__(self, nama, bintang):
        self.nama = nama  # Inisialisasi nama hotel
        self.bintang = bintang  # Inisialisasi jumlah bintang hotel

    def informasi(self):
        return f"Hotel: {self.nama}\nBintang: {self.bintang}"  # Mengembalikan informasi tentang hotel

class KamarHotel:
    def __init__(self, nomor_kamar, harga_malam):
        self.nomor_kamar = nomor_kamar  # Inisialisasi nomor kamar
        self.harga_malam = harga_malam  # Inisialisasi harga per malam kamar
        self.status = "Tersedia"  # Status awal kamar adalah tersedia

    def pesan_kamar(self, jumlah_malam, jumlah_tamu):
        if self.status == "Tersedia":
            total_harga = jumlah_malam * self.harga_malam
            if jumlah_tamu > 1:
                total_harga += 50.000 * jumlah_tamu  # Biaya tambahan per tamu
            return total_harga  # Mengembalikan total harga pesanan
        else:
            raise ValueError("Kamar sudah dipesan.")  # Melakukan raise exception jika kamar sudah dipesan

class KamarSingle(KamarHotel):
    def __init__(self, nomor_kamar):
        super().__init__(nomor_kamar, 100.000)  # Harga per malam untuk kamar single diinisialisasi melalui super()

    def informasi(self):
        return f"Kamar Single ({self.nomor_kamar}) - Harga per Malam: {self.harga_malam}"  # Mengembalikan informasi khusus kamar single

class KamarDouble(KamarHotel):
    def __init__(self, nomor_kamar):
        super().__init__(nomor_kamar, 150.000)  # Harga per malam untuk kamar double diinisialisasi melalui super()

    def informasi(self):
        return f"Kamar Double ({self.nomor_kamar}) - Harga per Malam: {self.harga_malam}"  # Mengembalikan informasi khusus kamar double
