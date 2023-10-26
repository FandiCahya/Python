from amkp.pengguna import orang

class sehat(orang):
    def __init__(self, nama=None, umur=None, tekanan_darah=0, gula_darah=0, kolesterol=0, asam_urat=0):
        super().__init__(nama, umur)
        self.tekanan_darah = tekanan_darah
        self.gula_darah = gula_darah
        self.kolesterol = kolesterol
        self.asam_urat = asam_urat

    def cek_kondisi_umum(self):
        return f"{self.nama}, umur {self.umur} tahun\nHasil Lab : \n-Tekanan darah {self.tekanan_darah} mmHg \n-Gula darah {self.gula_darah} mg/dL \n-Kolesterol {self.kolesterol} mg/dL \n-Asam urat {self.asam_urat} mg/dL"

    def cek_kesehatan_umum(self):
        kondisi = []
        if 90 <= self.tekanan_darah <= 120:
            kondisi.append("Tekanan darah dalam batas normal")
        else:
            kondisi.append("Perlu perhatian pada tekanan darah")
        if 70 <= self.gula_darah <= 100:
            kondisi.append("Gula darah dalam batas normal")
        else:
            kondisi.append("Perlu perhatian pada gula darah")
        if 120 <= self.kolesterol <= 200:
            kondisi.append("Kolesterol dalam batas normal")
        else:
            kondisi.append("Perlu perhatian pada kolesterol")
        if self.asam_urat < 6:
            kondisi.append("Asam urat dalam batas normal")
        else:
            kondisi.append("Perlu perhatian pada asam urat")
        return kondisi

    def berikan_saran(self):
        saran = []
        if self.tekanan_darah:
            if 90 <= self.tekanan_darah <= 120:
                pass
            elif self.tekanan_darah < 90:
                saran.append("Banyak makanan yang mengandung zat besi")
            else:
                saran.append("Kurangi garam dalam makanan Anda.")
        if self.gula_darah:
            if 70 <= self.gula_darah <= 100:
                pass
            elif self.gula_darah < 70:
                saran.append("Perbanyak konsumsi karbohidrat kompleks")
            else:
                saran.append("Kurangi makanan manis dan konsumsi karbohidrat kompleks.")
        if self.kolesterol:
            if 120 <= self.kolesterol <= 200:
                pass
            elif self.kolesterol < 120:
                saran.append("Konsumsi suplemen sesuai anjuran Dokter")
            else:
                saran.append("Kurangi makanan tinggi lemak jenuh dan kolesterol.")
        if self.asam_urat:
            if 3 <= self.asam_urat <= 6:
                pass
            else:
                saran.append("Kurangi makanan tinggi purin seperti daging merah dan alkohol.")
        return saran


    def input_data_kesehatan(self):
        try:
            self.tekanan_darah = int(input("Tekanan Darah (mmHg): "))
            self.gula_darah = int(input("Gula Darah (mg/dL): "))
            self.kolesterol = int(input("Kolesterol (mg/dL): "))
            self.asam_urat = float(input("Asam Urat (mg/dL): "))
            print("Data sudah diproses, silahkan lanjut pada menu nomor 3")
        except ValueError:
            print("Masukkan harus berupa angka.")
            
