''' Fungsi dengan argument (input)'''

# Template
# def nama_fungsi(argument):
#     Badan fungsi

def tambah(ang1,ang2):
    hasil = ang1+ang2
    print(f"{ang1}+{ang2}={hasil}")
tambah(2,4)

def say(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Baginda {peserta}")
oi=["Jamal","Baek","Jimin"]
say(oi)