from . import Operasi

def read_console():
    data_file = Operasi.read()
    
    index = "No"
    Nim = "NIM"
    Nama_Mahasiswa = "Nama Mahasiswa"
    Tempat_PKL = "Tempat PKL"
    Date_PKL = "Tanggal PKL"
    Lama_PKL = "Lama PKL"
    Pembimbing = "Nama Pembimbing"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {Nim:18} | {Nama_Mahasiswa:30} | {Tempat_PKL:20} | {Date_PKL:20} | {Lama_PKL:2} | {Pembimbing:20}")
    print("-"*100)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        Nim = data_break[0]
        Nama_Mahasiswa = data_break[1]
        Tempat_PKL = data_break[2]
        Date_PKL = data_break[3]
        Lama_PKL = data_break[4]
        Pembimbing = data_break[5]
        print(f"{index+1:4} | {Nim:18} | {Nama_Mahasiswa:30} | {Tempat_PKL:20} | {Date_PKL:20} | {Lama_PKL:2} | {Pembimbing:20}",end="")

    # Footer
    print("="*100+"\n")