class Mahasiswa:
    def __init__(self):
        self.nim = []
        self.nama = []
    
    def set_data(self,id,name):
        self.nim=id
        self.nama=name
        
    def tampil_data(self):
        print(f"NIM = {self.nim}")
        print(f"NAMA = {self.nama}")

class Kelompok(Mahasiswa):
    def __init__(self):
        self.id = []
        self.nama_kelompok = []

    def set_kel(self,id,nama):
        self.id = id
        self.nama_kelompok = nama
    
    def tampil_kel(self):
        print(f"Nama Kelompok = {self.nama_kelompok}")