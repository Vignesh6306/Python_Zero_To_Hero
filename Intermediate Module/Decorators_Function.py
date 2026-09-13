def decorator(func):
    def wrapper():
        print("It runs before the actual function")
        func()
        print("It run after the wrapper function")
    return wrapper

@decorator
def greeting():
    print("welcome to wrapper function")

greeting()

# Instead of Using this method to call the function and wrapper function use @First_Function_Name
#new_decorator = decorator(greeting)
#new_decorator()



