class Character:
    def __init__(self,name,health,attack,blood):
        self.name=name
        self.health=health
        self.attack = attack
        self.blood=blood
    def attack_enemy(self):
        print(f'{self.name}attacks with power {self.attack} with blood {self.blood}')
warrior = Character("Thor",100,50,"B+ve")
Mage=Character("delf",80,70,"A+ve")
warrior.attack_enemy()
Mage.attack_enemy()