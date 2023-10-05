class hero:
    # Class Variable / Static Variable
    jumlah = 0
    def __init__(self,inputname,inputhealth,inputpower,inputarmor):
        # Instance Variable
        self.name = inputname 
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor
        # Pemangilan Class jumlah
        hero.jumlah += 1
        
    #Method tanpa return,tanpa argumen 
    def siapa(self):
        print(f"Nama Heroku Adalah {self.name}")
        
    # Method dengan argumen,tanpa return
    def healthUp(self,up):
        self.health += up
    
    # Method dengan return
    def getHealth(self):
        return self.health

hero1 = hero("Supri",100,30,70)
hero2 = hero("Bambang",100,20,30)
hero3 = hero("Gaguk",100,90,30)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())


