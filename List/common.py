# common elements in both list

a=[1,2,3,4]
b=[6,7,8,3]
#set function
s1 = set(a)
s2= set(b)
#intersect both sets to find common
s3=s1.intersection(s2)
print(list(s3))