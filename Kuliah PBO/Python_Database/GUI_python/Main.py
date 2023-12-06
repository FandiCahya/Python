from User import User
from Barang import Barang

def greeting():
    print("="*40)
    print("SELAMAT DATANG DI APLIKASI KASIR APOTEK")
    print("="*40)

def menu_admin():
    print(">> Menu Admin")
    print("1) Lihat data user \n2) Tambah data user \n3) Edit data user \n4) Delete data user \n5) Logout")

def menu_kasir():
    print(">> Menu Kasir")
    print("1) Lihat data barang \n2) Tambah data barang \n3) Edit data barang \n4) Delete data barang \n5) Logout")

def login():
    print("\nSilahkan masukkan username dan password")
    usernamelogin=input("Username : ")
    passwordlogin=input("Password : ")
    level_login=usr.login(usernamelogin, passwordlogin)
    return level_login

usr = User
brg = Barang
greeting()
level_login=login()

menu_berlanjut=True
while(menu_berlanjut):
    if(level_login.lower() == "admin"):
        menu_admin()
        menu=int(input("Masukkan menu yang Anda Inginkan : "))
        if(menu==1):
            usr.select_data()
        elif(menu==2):
            nama_baru=input("Masukkan nama : ")
            username_baru=input("Masukkan username : ")
            password_baru=input("Masukkan password : ")
            level_baru=input("Masukkan level : ")
            usr.insert_data(nama_baru,username_baru,password_baru,level_baru)
        elif(menu==3):
            username=input("Masukkan username yang akan diganti datanya : ")
            nama_baru=input("Masukkan nama : ")
            password_baru=input("Masukkan password : ")
            level_baru=input("Masukkan level : ")
            usr.update_data(nama_baru,password_baru,level_baru,username)
        elif(menu==4):
            username=input("Masukkan username yang akan dihapus datanya : ")
            usr.delete_data(username)
        elif(menu==5):
            level_login=login()
        else:
            menu_berlanjut=False
        
    elif(level_login.lower() == "kasir"):
        menu_kasir()
        menu=int(input("Masukkan menu yang Anda Inginkan : "))
        if(menu==1):
            brg.select_data()
        elif(menu==2):
            id_baru=input("Masukkan id : ")
            nama_baru=input("Masukkan nama : ")
            stok_baru=input("Masukkan stok : ")
            harga_baru=input("Masukkan harga : ")
            brg.insert_data(id_baru,nama_baru,stok_baru,harga_baru)
        elif(menu==3):
            id=input("Masukkan id yang akan diganti datanya : ")
            nama_baru=input("Masukkan nama : ")
            stok_baru=input("Masukkan stok : ")
            harga_baru=input("Masukkan harga : ")
            brg.update_data(nama_baru,stok_baru,harga_baru,id)
        elif(menu==4):
            id=input("Masukkan id yang akan dihapus datanya : ")
            brg.delete_data(id)
        elif(menu==5):
            level_login=login()
        else:
            menu_berlanjut=False
    else:
        print("Hanya ada Kasir dan Admin Ganzz!!!!")
        break