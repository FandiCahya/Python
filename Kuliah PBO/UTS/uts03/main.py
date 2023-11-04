from pengguna import Junior,Senior

def main():
    junior = Junior("Junior")
    senior = Senior("Senior")
    senior.tambah_informasi(123, "Informasi")
    senior.tambah_komentar(123, "Komentar 1")

    senior.menu()
    print(junior.status)
    print(senior.status)

main()