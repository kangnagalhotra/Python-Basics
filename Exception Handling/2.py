try:
    file = open("/Users/kanganagalhotra/Desktop/Python/Exception Handling/error.txt",'r')
    content = file.read()
    print(content)

except FileNotFoundError:
    print("file not found")

finally:
    file.close()
    print("File operation done")