# Global Variable : can be used and called anywhere in the program
x = 10
print(x)

# Local Variable : Only can Called inside the function
def Local():
    y = 5
    print(y)

Local()
# print(y) -> Cannot be possible. Because y was Declared as local
print(x)

# Example - 2

A = 25
print(A)

def local():
    global A  # Declare a Global Variable inside the function using global keyword
    A = 20
    print(A)

local()
print(A)
