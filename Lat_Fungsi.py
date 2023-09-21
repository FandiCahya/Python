import os
# Fungsi Header
def header():
    os.system("cls")
    print(f"{'PROGRAM MENGITUNG':^40}")
    print(f"{'LUAS DAN KELILING LINGKARAN':^40}")
    print(f"{'='*40:^40}")
    
# Fungsi Input User
def inp_user():
    jari2 = float(input("Masukkan Nilai Jari-Jari: "))
    
    return jari2

# Fungsi Perhitungan Luas
def hitung_luas(jari2):
    luas = 3.14 *jari2**2
    return luas
# Fungsi Perhitungan Keliing
def hitung_keliling(jari2):
    keliling = 2*3.14*jari2
    return keliling
# Fungsi Display
def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")

# Program Utamanya
while True:
    header()
    print("1.Luas\n2.Keliling")
    opsi = input("Masukksan Opsi anda : ")
    JARI = inp_user()
    if opsi == "1" :   
        LUAS = hitung_luas(JARI)
        display("Luas",LUAS)
    else:    
        KELILING = hitung_keliling(JARI)
        display ("Keliling",KELILING)
    
    iscont = input("Apakah Ingin Lanjut (y/n)")
    if iscont == "n":
        break
print("AKHIR DARI PROGRAM")