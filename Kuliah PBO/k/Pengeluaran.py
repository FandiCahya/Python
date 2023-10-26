import Pemasukan
import json
import datetime

p = Pemasukan.Pemasukan
now = datetime.datetime.now()
dt = now.strftime("%d-%m-%Y %H:%M:%S")

class Pengeluaran(p):

    def pengeluaran():
        nb = []
        try:
            with open("data.json","r") as data:
                file = json.load(data)
                pass
        except:pass

        jp = input("Jenis Pengeluaran : ")
        while True:
            try :
                bb = int(input("Banyak Barang : "))
                break
            except :
                print("Masukan harus berupa angka")

        for i in range(bb):
            ok = input(f"Nama barang ke {i+1} : ")
            nb.append(ok)

        while True:
            try :
                tb = int(input("Total Pengeluaran : "))
                break
            except :
                print("Masukan harus berupa angka")

        data_new = {
            "tanggal" : dt,
            "jenis_pengeluaran" : jp,
            "banyak_barang": bb,
            "nama_barang" : nb,
            "jumlah" : tb
        }

        file["pengeluaran"].append(data_new)
        
        try:
            with open("data.json","w") as data:
                json.dump(file,data)
                print("Data berhasil di tambahkan")
        except:pass
        pass
        
    def lihat():
        print("\nDATA PENGELUARAN : ")
        nul = p.kosong()
        if nul:
            print("Data Kosong")
        else: 
            uang = 0
            with open("data.json","r")as file:
                data = json.load(file)
            
            pengeluaran = data["pengeluaran"]

            # print(pengeluaran)
            for nilai in pengeluaran:
                print(f"Tanggal            : {nilai['tanggal']}")
                print(f"Jenis Pengeluaran  : {nilai['jenis_pengeluaran']}")
                print(f"Banyak barang      : {nilai['banyak_barang']}")
                print(f"Jumlah Pengeluaran : {nilai['jumlah']} \n")
                # break

            for money in pengeluaran:
                total = money['jumlah']
                uang += total
            print(f"Perkiranan Pengeluaran semuanya = {uang}")
