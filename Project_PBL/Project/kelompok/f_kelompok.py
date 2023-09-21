data_kelompok = []
# Fungsi untuk menambah data kelompok
def tambah_kelompok(id_kelompok, nama_instansi, lama_pkl, list_nim):
    # Temukan instansi berdasarkan id_instansi
    instansi = None
    for data in data_instansi:
        if data["nama_instansi"] == nama_instansi:
            instansi = data
            break

    if instansi is None:
        print("Instansi dengan nama tersebut tidak ditemukan.")
        return

    # Temukan mahasiswa berdasarkan NIM
    mahasiswas_kelompok = []
    for nim in list_nim:
        found = False
        for data in data_mhs:
            if data["nim"] == nim:
                mahasiswas_kelompok.append(data)
                found = True
                break
        if not found:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    data_kelompok.append({
        "id_kelompok": id_kelompok,
        "nama_instansi": instansi["nama_instansi"],
        "lama_pkl": lama_pkl,
        "list_nim": [mhs["nim"] for mhs in mahasiswas_kelompok]
    })

    print("Data kelompok berhasil ditambahkan.")


# Fungsi untuk melihat data kelompok
def lihat_kelompok():
    for kelompok in data_kelompok:
        print("="*20)
        print("ID Kelompok:", kelompok["id_kelompok"])
        print("Nama Instansi:", kelompok["nama_instansi"])
        print("Lama PKL:", kelompok["lama_pkl"]," Bulan")
        print("NIM dalam Kelompok:", kelompok["list_nim"])
        print("="*20)
        print("")

# Fungsi menu untuk mengelola data kelompok
def menu_kelompok():
    while True:
        print("\n===== Menu Kelola Data Kelompok =====")
        print("1. Tambah Kelompok")
        print("2. Lihat Kelompok")
        print("3. Kembali ke Menu Admin")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_mahasiswa()
            lihat_instansi()
            id_kelompok = input("ID Kelompok: ")
            nama_instansi = input("Nama Instansi : ")
            lama_pkl = input("Lama PKL: ")
            list_nim = input("NIM dalam Kelompok (pisahkan dengan koma): ").split(",")
            tambah_kelompok(id_kelompok, nama_instansi,lama_pkl, list_nim)
        elif pilihan == "2":
            lihat_kelompok()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
