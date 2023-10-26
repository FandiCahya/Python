class TiketTravel:
    def __init__(self, kelas, jumlah_tiket, harga_per_tiket):
        self.kelas = kelas
        self.jumlah_tiket = jumlah_tiket
        self.harga_per_tiket = harga_per_tiket

    def tampilan(self):
        return f"Kelas: {self.kelas} \nJumlah Tiket: {self.jumlah_tiket}"

class TiketHaji(TiketTravel):
    def __init__(self, jumlah_tiket):
        super().__init__("Haji", jumlah_tiket, 50000000)  # Harga tiket Haji

    def pesan_tiket(self):
        if self.jumlah_tiket <= 5:
            print(f"Berhasil memesan {self.jumlah_tiket} tiket kelas Haji.")

class TiketUmroh(TiketTravel):
    def __init__(self, jumlah_tiket):
        super().__init__("Umroh", jumlah_tiket, 32000000)  # Harga tiket Umroh

    def pesan_tiket(self):
        if self.jumlah_tiket <= 5:
            print(f"Berhasil memesan {self.jumlah_tiket} tiket kelas Umroh.")

class Pembayaran:
    def __init__(self, tiket):
        self.tiket = tiket
        self.hitung_harga()

    def hitung_harga(self):
        self.total_harga = self.tiket.jumlah_tiket * self.tiket.harga_per_tiket

    def bayar(self):
        print(f"Total harga: Rp.{self.total_harga}  \nSilahkan bayar.")
        print(f"Terima Kasih Sudah Mengunjungi Aplikasi Kami")