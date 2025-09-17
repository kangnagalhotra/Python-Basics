#method override
class bird():
    def sound(self):
        print("birds make sound")
class Crow(bird):
    def sound(self):
        print("Crows make caw caw sound")
class  Parrot(bird):
    def sound(self):
        print("Parrot make squak sound")
        
bird1 = Crow()
bird2=Parrot()

bird1.sound()
bird2.sound()
    
    