squares =[]
for i in range(1,11):
    squares.append(i ** 2)
print(squares)

#single line
squares2=[i**2 for i in range(1,11) if i%2==0]
print(squares2)