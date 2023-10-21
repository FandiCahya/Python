class Instansi:
    def __init__(self):
        self.id = []
        self.nama_ins = []
    
    def set_data(self,id,name):
        self.id=id
        self.nama_ins=name
        
    def tampil_data(self):
        print(f"Nama Instansi = {self.nama_ins}")