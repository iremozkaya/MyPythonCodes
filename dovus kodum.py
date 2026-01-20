class Fighter:
    def __init__(self,name,health,damage):
        self.name=name
        self.health=health
        self.damage=damage

    def attacks(self,opponent):
        print(f"{self.name} attacks {opponent.name}")
        opponent.takes_damage(self.damage)
        
    def takes_damage(self,damage):
        self.health-=damage
        if self.health<0:
            self.health=0
        print(f"{self.name} health: {self.health}")

    def is_alive(self):
        if self.health==0:
            return False
        else:
            return True
        


class Scorpion(Fighter):
    def __init__(self,name,health,damage):
        super().__init__(name,health,damage)

    def special_attack(self,opponent):
        print(f"{self.name} uses ice to {opponent.name}")
        opponent.takes_damage(self.damage+5)

class SubZero(Fighter):
    def __init__(self,name,health,damage):
        super().__init__(name,health,damage)

    def special_attack(self,opponent):
        print(f"{self.name} hell flame {opponent.name}")
        opponent.takes_damage(self.damage+10)     




secim=int(input("1. karakter secimi "))
if secim==1:
    player1=Scorpion("scorpion1",100,15)
elif secim==2:
    player1=SubZero("subzero1",100,20)

secim=int(input("2. karakter secimi "))
if secim==1:
    player2=Scorpion("scorpion2",100,15)
elif secim==2:
    player2=SubZero("subzero2",100,20)
else:
    print("hata")

player1_hak=2
player2_hak=2

while player1.is_alive() and player2.is_alive():

    while 1:
        hamle=int(input("hamle "))
        if hamle==1:
            player1.attacks(player2)
            break
        elif hamle==2:
            if player2_hak!=0:
                player1.special_attack(player2)
                player1_hak-=1
                break
            elif player1_hak==0:
                print("special hak bitti.")
        
    if not player2.is_alive():
        print(player1.name,"wins!")
        break
    
    while 1:
        hamle=int(input("hamle "))
        if hamle==1:
            player2.attacks(player1)
            break
        elif hamle==2:
            if player2_hak!=0:
                player2.special_attack(player1)
                player2_hak-=1
                break
            elif player2_hak==0:
                print("special hak bitti.")
    


else:
    if player1.health!=0:
        print(player1.name,"wins!")
    else:
        print(player2.name,"wins!")