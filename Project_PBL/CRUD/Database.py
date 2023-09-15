from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "Nim":16*"",
    "Nama_Mahasiswa":255*" ",
    "Tempat_PKL":255*" ",
    "date_PKL":"yyyy-mm-dd",
    "Lama_PKL":" ",
    "Pembimbing":255*" "
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Data tersedia !")
    except:
        print("Data Kosong, silahkan masukkan data dahulu")
        Operasi.create_first_data()
        
            