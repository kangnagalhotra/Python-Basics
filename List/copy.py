list1=[1,2,3,4]
list2 = list1.copy()
list2[0]=100
print(list1,list2)
#only change in list2 not in list1 because we made copy of list1 (not original list1 is used)