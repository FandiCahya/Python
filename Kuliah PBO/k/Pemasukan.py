import json
import datetime

now = datetime.datetime.now()
dt = now.strftime("%d-%m-%Y %H:%M:%S")

class Pemasukan:

    def pemasukan():
        try:
            with open("data.json","r") as data:
                file = json.load(data)
                pass
        except:pass

        while True:
            sp= input("Sumber Pendapatan : ")
            try : 
                jumlah = int(input("Jumlah : "))
                break
            except:
                print("Jumlah harus berupa angka")
            break

        data_new = {
            "tanggal" : dt,
            "sumber" : sp,
            "jumlah" : jumlah
        }

        file["pemasukan"].append(data_new)
        
        try:
            with open("data.json","w") as data:
                json.dump(file,data)
                print("Data berhasil di tambahkan")
        except:pass

    def lihat():
        print("DATA PEMASUKAN : ")
        nul = Pemasukan.kosong()
        if nul : 
            print("Data masih kosong")
        else :
            uang = 0
            with open("data.json","r")as file:
                data = json.load(file)
            
            pemasukan = data["pemasukan"]

            # print(pemasukan)
            for nilai in pemasukan:
                print(f"Tanggal : {nilai['tanggal']}")
                print(f"Sumber  : {nilai['sumber']}")
                print(f"Nominal : {nilai['jumlah']} \n")
            for money in pemasukan:
                total = money['jumlah']
                uang += total
            print(f"Perkiranan Pemasukan semuanya = {uang}")

    def kosong():
        with open("data.json","r") as file:
            data = json.load(file)

        if len(data["pemasukan"]) == 0 or len(data["pengeluaran"]) == 0:
            return True
