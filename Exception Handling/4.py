#CHeck password strength
def checkPass(password):
    if len(password)<8:
        raise Exception("Error : password must be <=8")   #custom excep raised
    print("Password is strong")
try:
    password = input("Enter passeord")
    checkPass(password)
except Exception as e:
    print(e)
    