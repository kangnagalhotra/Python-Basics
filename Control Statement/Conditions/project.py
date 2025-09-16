num_1 = float(input("enter float number 1: "))
num_2 = float(input("enter float number 2: "))

choice = input('Enter your choice + - * / // %  **: ')

#f"" → tells Python “this is a formatted string, evaluate anything inside { }”

if choice == '+':
    print(f"Addition: {num_1 + num_2}")
elif choice == '-':
    print(f"Subtraction: {num_1-num_2}")
elif choice == '*':
    print(f"Multiplication: {num_1 * num_2}")
elif choice =='/':
    print(f"Divide: {num_1/num_2}")
elif choice =='%':
    print(f"Modulus: {num_1/num_2}")
elif choice =='**':
    print(f"Exponential: {num_1**num_2}")
else:
    print("Invalid")


    
    