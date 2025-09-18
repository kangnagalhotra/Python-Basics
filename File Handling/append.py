with open("/Users/kanganagalhotra/Desktop/Python/File Handling/file2.txt",'a') as file:
    
    content = input("enter data: ")
    file.write(content)
    print("Data appended successfully")
    file.close()
