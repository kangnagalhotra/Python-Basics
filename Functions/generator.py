'''
vending machine - what you will select it will give that product
on demand value is generated

A normal function in Python uses return → it ends the function immediately.

A generator function uses yield → it pauses the function and remembers where it left off. 
Next time you call it, it continues from there.
'''

def count_down(num):
    while num>0:
        yield num #yield values one at a time
        num = num-1
#using generator
for number in count_down(5):
    print(number)   