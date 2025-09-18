try:
    num1 = int(input("Enter number"))
    num2 = int(input("Enter number"))
    try:
        result = num1/num2
        print(f'{result}')
    except ZeroDivisionError:
        print("you cannot divide by zero")
except ValueError:
    print("You cannot divide by another datatype")
    
