class car():
    def set_details(self,brand,color):
        self.brand= brand
        self.color= color
    def show_details(self):
        print(f'this is a {self.brand} {self.color}')
        
car1=car()
car2=car()

car1.set_details("BMW","red")
car2.set_details("Tesla","green")

car1.show_details()
car2.show_details()

