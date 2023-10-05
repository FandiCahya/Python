data_profil = []  # Memulai dengan list kosong
cache_login = {"nama": "", "nik": "", "no_tel": "", "password": ""}  # Cache login
riwayat_pengajuan = []  # Riwayat pengajuan

perulangan = "ya"
logged_in = False

def regis():
    global cache_login
    nama = input("Masukkan nama:")
    nik = input("Masukkan NIK:")
    no_tel = input("Masukkan nomor telepon:")
    password = input("Masukkan password:")
    data_profil.append({"nama": nama, "nik": nik, "no_tel": no_tel, "password": password})
    # cache_login = {"nama": nama, "nik": nik, "no_tel": no_tel, "password": password}

def login():
    global logged_in
    global cache_login
    nama = input("Masukkan nama untuk login:")
    password = input("Masukkan password untuk login:")
    for profil in data_profil:
        if profil["nama"] == nama and profil["password"] == password:
            logged_in = True
            cache_login = profil
            print(f"Selamat datang, {profil['nama']}!")
            return
    print("Data tidak ditemukan. Silakan registrasi terlebih dahulu.")

def lihat_profil():
    for profil in data_profil:
        if profil["nama"] == cache_login["nama"]:
            print("nama:", profil['nama'])
            print("NIK:", profil['nik'])
            print("No telp:", profil['no_tel'])

def edit_profil():
    global cache_login
    lihat_profil()
    print("Edit Profil:")
    cache_login["nama"] = input(f"Ganti nama ({cache_login['nama']}):") or cache_login["nama"]
    cache_login["no_tel"] = input(f"Ganti nomor telepon ({cache_login['no_tel']}):") or cache_login["no_tel"]
    cache_login["password"] = input(f"Ganti password ({cache_login['password']}):") or cache_login["password"]

    # Perbarui data di data_profil
    for profil in data_profil:
        if profil['nik'] == cache_login['nik']:
            profil.update(cache_login)  # Perbarui data dengan cache_login
            break
    print("Profil berhasil diubah.")

def pengajuan_berkas():
    global cache_login
    global riwayat_pengajuan
    print("Pengajuan Berkas:")
    print("1. Perubahan data KTP")
    print("2. Surat Kelakuan Baik")
    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        nik_lama = input("Masukkan NIK lama:")
        # Tambahkan logika untuk perubahan data KTP di sini
        print("Pengajuan Perubahan data KTP telah diajukan.")
        riwayat_pengajuan.append(f"{cache_login['nama']} mengajukan perubahan data KTP")
    elif pilihan == "2":
        print("Surat Kelakuan Baik telah diajukan.")
        riwayat_pengajuan.append(f"{cache_login['nama']} mengajukan surat kelakuan baik")

def tampilkan_riwayat_pengajuan():
    print("Riwayat Pengajuan:")
    for i, pengajuan in enumerate(riwayat_pengajuan, 1):
        print(f"{i}. {pengajuan}")

while perulangan != "tidak":
    print("")
    print("1. Registrasi")
    print("2. Login")
    print("3. Pengajuan Berkas")
    print("4. Tampilkan Riwayat Pengajuan")
    # print("99. Menu Admin")
    pilihan = input("Pilih menu (1/2/3/4/exit): ")

    if pilihan == "1":
        regis()
    elif pilihan == "2":
        while perulangan != "tidak":
            if logged_in:
                print(f"Selamat datang, {cache_login['nama']}!")
                print("1. Lihat Profil")
                print("2. Edit Profil")
                print("3. Logout")
                pilihan = input("Pilih menu (1/2/3): ")
                if pilihan == "1":
                    lihat_profil()
                elif pilihan == "2":
                    edit_profil()
                elif pilihan == "3":
                    logged_in = False
            else:
                login()
            break
    elif pilihan == "3":
        pengajuan_berkas()
    elif pilihan == "4":
        tampilkan_riwayat_pengajuan()
    elif pilihan == "99":
        # Tambahkan logika untuk menu admin di sini
        pass
    elif pilihan == "exit":
        perulangan = "tidak"
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
