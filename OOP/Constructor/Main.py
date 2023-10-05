class hero:

    def __init__(self,inputname,inputhealth,inputpower,inputarmor):
        # Instance Variable
        # ini sama dengan hero("Supri")
        self.name = inputname 
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor

hero1 = hero("Supri",100,30,70)
hero2 = hero("Bambang",100,20,30)
hero3 = hero("Gaguk",100,90,30)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)