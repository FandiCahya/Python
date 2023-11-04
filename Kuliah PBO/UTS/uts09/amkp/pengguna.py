class orang:
    def __init__(self, nama=None, umur=None):
        self.nama = nama
        self.umur = umur

    def cek_kondisi_umum(self):
        return f"Saudara {self.nama}, umur {self.umur} tahun, silahkan isi menu nomor 2"
    
    def daftar(self):
        print("Masukkan nama dan umur anda")
        nama = input("Nama : ")
        umur = int(input("Umur : "))
        self.nama = nama
        self.umur = umur
        return self.nama, self.umur