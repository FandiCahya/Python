## Tutorial membaca file eksternal

print(3*"=", " Membaca file txt ", 3*"=")
file = open("E:\Python\TutoriaL_Dasar\Membaca File\data.txt",mode="r")

print(f"Status Read : {file.readable()}")
print(f"Status Write : {file.writable()}")

# Membaca Seluruh File
print(file.read())

## baca per baris
# print(file.readline(),end="") # baca baris pertama
# print(file.readline(),end="") # baca baris kedua

## baca semua baris sebagai list
# print(file.readlines())

print(f"Apakah File sudah di close : {file.closed}")
file.close()
print(f"Apakah File sudah di close : {file.closed}")

## salah satu teknik membuka file di python

print("\n",3*"=", " Membaca file txt dengan with", 3*"=")
with open("E:\Python\TutoriaL_Dasar\Membaca File\data.txt",mode="r")as file:
    content = file.read()
    print(content,end="")
    print(f"Apakah File sudah di close : {file.closed}")
print(f"Apakah File sudah di close : {file.closed}")