try:
    num = int (input("enter number"))
    result = 10/num
    print(f'{result}')
    
except ZeroDivisionError:
    print("you cannot divide with 0")
    
except ValueError:
    print("you cannot divide with string")
    


