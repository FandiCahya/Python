import datetime
import json
""" PROGRAM MONITORING LAPORAN KEUANGAN PRIBADI 

1. TAMPILAN MENU : PEMASUKAN,PENGELUARANM,CETAK 
CR PEMASUKAN SUPERCLASS => PENGELUARAN SUBCLASS
CETAK => EXCEPTION

"""
""" 
def menu():
    pass

def read():
    pass

def tambah():
    pass

def cetak():
    pass
 """

x = datetime.datetime.now()

p = x.strftime("%d-%m-%Y %H:%M:%S")

# with open("in.txt","r") as file :
#     for i in file :
#         bag = i.strip.split(" ")
#     pass

# data ={
#     "Pengeluaran" : [
#         {
#             "nama" : "Amdzak",
#             "usia" : 29,
#             "asal" : "Mlg"
#         }
#     ],
#     "Pemasukan" : [
#         {
#             "nama" : "kucing",
#             "usia" : 10,
#             "harga" : 2000
#         }
#     ]
# }

# with open("dat.json","w") as file :
#     json.dump(data,file)

with open("dat.json","r") as file :
    data_baru = json.load(file)

new ={
            "nama" : "kucing2",
            "usia" : 9,
            "harga" : "1000"
        }
data_baru["Pemasukan"].append(new)

with open("dat.json","w") as file :
    json.dump(data_baru,file)

# data_baru.append(new)

# with open("data3.json","w") as file :
#     json.dump(data_baru,file)

# print(data_baru)
# print(f"Usia : {data_baru[-1]['Hewan'][0]['usia']} bulan")

def total():
        pemasukan = []
        pengeluaran = []
        try:
            with open("data.json","r")as file:
                data = json.load(file)
        except:pass

        tgl_pem = data["pemasukan"][-1]["tanggal"]
        jum_pem = data["pemasukan"][-1]["jumlah"]
        pemasukan.append(tgl_pem)
        pemasukan.append(jum_pem)

        tgl_pen = data["pengeluaran"][-1]["tanggal"]
        pengeluaran.append(tgl_pen)
        tgl_pen = data["pengeluaran"][-1]["banyak_barang"]
        pengeluaran.append(tgl_pen)
        tgl_pen = data["pengeluaran"][-1]["jumlah"]
        pengeluaran.append(tgl_pen)

        data_new = {
            "tanggal" : p,
            "pemasukan" : pemasukan,
            "pengeluaran" : pengeluaran
        }

        data["total"].append(data_new)
        try:
            with open("data.json","w") as lap:
                json.dump(data,lap)
                print("Data berhasil di tambahkan")
        except:pass