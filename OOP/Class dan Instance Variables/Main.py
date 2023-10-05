class hero:
    # Class Variable / Static Variable
    jumlah = 0
    def __init__(self,inputname,inputhealth,inputpower,inputarmor):
        # Instance Variable
        # ini sama dengan hero("Supri")
        self.name = inputname 
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor
        # Pemangilan Class jumlah
        hero.jumlah += 1
        print(f"Membuat Hero dengan nama {self.name}")

hero1 = hero("Supri",100,30,70)
print(hero1.jumlah)
hero2 = hero("Bambang",100,20,30)
print(hero1.jumlah)
hero3 = hero("Gaguk",100,90,30)
print(hero1.jumlah)

# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)