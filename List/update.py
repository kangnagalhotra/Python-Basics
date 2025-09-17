#single value update
list =[1,2,3,4]
print("Before " , list)
list[0]="hello"
print("After" , list)

#multiple value update (slicing)
list2 = [1,2,3,4,5]
list2[0:3]= 10,20,30
print(list2)
