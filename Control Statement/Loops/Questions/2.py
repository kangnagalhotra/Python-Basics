# ask user which number to skip
start = int(input("Enter a start number"))
stop = int(input("Enter a stop number"))
skip =int(input("Enter which number you want to skip"))

if start>=stop:
    print("Invalid")
else:
    if skip not in range(start,stop):
        print("Skip is not in range")
    else:
        for i in range(start,stop):
            if(i==skip):
                continue
            print(i)
    
    
