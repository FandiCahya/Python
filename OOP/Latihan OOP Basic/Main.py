class Hero:
    def __init__(self,name,health,power,armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
    def serang(self,enemy):
        print(self.name+" DiSerang "+enemy.name)
        enemy.diserang(self,self.power)

    def diserang(self,enemy,power_enemy):
        print(self.name+" DiSerang "+enemy.name)
        att_diterima= power_enemy-self.armor
        print("Serangan Terasa : "+ str(att_diterima))
        self.health -= att_diterima
        print("darah "+self.name+" tersisa "+ str(self.health))

sniper = Hero('sniper',100,10,5)
rikimaru = Hero('rikimaru',100,20,10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)