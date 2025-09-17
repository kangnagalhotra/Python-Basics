'''
burger - function
extra cheese - feature

main function - add new function without changing original function this is decorator
'''

def my_decorator(func):
    def wrapper():
        print("Something is happing before function is called")
        func() #@my_decorator
        print("Something is happening after function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
say_hello()