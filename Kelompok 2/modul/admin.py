def admin():
    a = 1
    for profil in data_profil:
        print(f"{a}. {profil['nama']}")
        print(f"   No Telepon: {profil['telepon']}")
        print(f"   NIK       : {profil['nik']}")
        print(f"   Password  : {profil['password']}")
        a += 1
    
        hapus = input("Masukkan NIK yang akan dihapus:")
        if hapus == profil["nik"]:
            data_profil.remove(profil)
            print(f"Profil dengan NIK {hapus} berhasil dihapus.")
            return
    print(f"Tidak ada profil dengan NIK {hapus}.")