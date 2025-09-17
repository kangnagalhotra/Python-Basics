class student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
#objects
student1 = student("Rakesh",20,"A+")
student2=student("Lokesh",20,"C+")

print(student1.name,student1.age,student1.grade)
print(student2.name,student2.age,student2.grade)