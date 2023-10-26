
class jadwal:
    def __init__(self, list_jadwal=[]):
        self.list_jadwal = list_jadwal

    def lihat_jadwal(self):
        print(" ")
        print("Jadwal :")
        print("="*30)
        for i, event in enumerate(self.list_jadwal, 1):
            print(f"{i}. {event['Waktu']} - {event['Acara']}")
        print("="*30)

class acara(jadwal):
    def __init__(self, list_jadwal=[]):
        super().__init__(list_jadwal)

    def tambah_acara(self, waktu, acara, id_acara):
        self.list_jadwal.append({"id": id_acara, "Waktu": waktu, "Acara": acara})
        print("=== Berhasil Menambahkan acara === ")

    def ubah_acara(self, index, waktu, acara):
        if index < len(self.list_jadwal):
            self.list_jadwal[index] = {"Waktu": waktu, "Acara": acara}
            print("=== Berhasil Mengubah acara === ")
        else:
            print("Indeks diluar jangkauan.")

    def hapus_acara(self, index):
        if index < len(self.list_jadwal):
            del self.list_jadwal[index]
            print("=== Berhasil Mennghapus acara === ")
        else:
            print("Indeks diluar jangkauan.")
            
    def lihat_jadwal(self):
        print(" ")
        print("Jadwal :")
        print("="*30)
        for i, event in enumerate(self.list_jadwal, 1):
            print(f"{i}. {event['Waktu']} - {event['Acara']}")
        print("="*30)
