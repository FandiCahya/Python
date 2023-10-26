try:
    x = int(input("Masukkan bilangan bulat pertama: "))
    y = int(input("Masukkan bilangan bulat kedua: "))

    result = x / y
    print(f"Hasil pembagian: {result}")

# except ZeroDivisionError as e:
#     print(f"Terjadi kesalahan: {e}. Tidak dapat melakukan pembagian dengan nol.")

except ArithmeticError as e:
    print(f"Terjadi kesalahan aritmatika: {e}. Pastikan operasi aritmatika valid.")

# 1
