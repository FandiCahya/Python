class jadwal:
    def __init__(self, list_jadwal):
        self.list_jadwal = list_jadwal
    
    def lihat_jadwal(self) :
        print("Jadwal :")
        for event in self.list_jadwal:
            print(f"{event['Waktu']} - {event['Acara']}")

class acara(jadwal):
    def __init__(self, list_jadwal=[]):
        super().__init__(list_jadwal)

    def tambah_acara(self, waktu, acara):
        self.list_jadwal.append({"Waktu": waktu, "Acara": acara})
