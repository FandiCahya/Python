class mahasiswa:
    def __init__(self):
        self.nim = []
        self.nama = []
    
    def set_data(self,id,name):
        self.nim=id
        self.nama=name
    def tampil_data(self):
        print(f"NIM = {self.nim}")
        print(f"NAMA = {self.nama}")

class aktivis(mahasiswa):
    def __init__(self):
        mahasiswa.__init__(self)
        self.org = []
    
    def set_org(self,org):
        self.org = org
    
    def tampil_org(self):
        print(f"Organisai = {self.org}")
    

mhs1 = mahasiswa()
mhs2 = mahasiswa()
mhs3 = aktivis()

mhs1.set_data(1,"Fandi")
mhs2.set_data(2,"Raka")
mhs3.set_data(3,"Vahya")
mhs3.set_org("MIMPI")

mhs1.tampil_data()
mhs2.tampil_data()
mhs3.tampil_data()
mhs3.tampil_org()