'''
__init__()
'''
class car():
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
#value automatically set
car1 = car("BMW","red")
print(car1.brand,car1.color)