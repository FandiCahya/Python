import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "nt": os.system("cls")

print("+"*4,"SISTEM INFORMASI",4*"+")
print(" ","+"*5,"Regulasi PKL",5*"+")
print("=============================")

username = input("Masukkan Username Anda : ")
password = input("Masukkan ")

# check database itu ada atau tidak
CRUD.init_console()

while(True):
    match sistem_operasi:
        case "nt": os.system("cls")

    print("+"*4,"SISTEM INFORMASI",4*"+")
    print(" ","+"*5,"Regulasi PKL",5*"+")
    print("=============================")
    
    print(f"1. Tampilkan Data")
    print(f"2. Tambah Data")
    print(f"3. Update Data")
    print(f"4. Update Data")
    
    user_in = input("Masukkan Pilihan Anda ?")
    
    print("\n=============================\n")
    
    match user_in :
        case "1" : CRUD.read_console()
        case "2" : print("Bambang")
        case "3" : print("Bambang")
        case "4" : print("Bambang")
        
    print("\n=============================\n")
    is_end = input("Apakah anda ingin Keluar (y/n) ?")
    if is_end == "y" or is_end == "Y" or is_end == "ya" or is_end =="yes":
        break

print("Program Berakhir")