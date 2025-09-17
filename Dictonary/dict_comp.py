#dict comprehension
squares = {x: x*x for x in range(1,11) if x%2==0}
print(squares)