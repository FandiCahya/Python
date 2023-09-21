''' Fungsi dengan kembalian'''

# template fungsi dengan kembalian
# def nama_fungsi(argument):
#       badan fungsi
#       return output

def kuadrat(inp):
    out = inp **3
    return out
print(kuadrat(5))

# fungsi tambah

def fungsi_tambah(angka_1,angka_2):
    '''fungsi return dengan multi input'''
    return angka_1 + angka_2

a = fungsi_tambah(10,8)
print(a)

# fungsi dengan return banyak

def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(9,5)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")