# To define a fuction use def and name the function then call by the function name
def greeting():
    print("Welcome to python")

greeting()

def Addition(A,B):
    C = A+B
    print(C)

Addition(10,20)

# Defining a function using return in it

def validation(age):
    if age >= 18:
        return 'Eligible to vote'
    else:
        return 'Not Eligible to vote'

result = validation(100)
print(result)
