# Recursive Function : It Calls By itself. The maximum repeatation of calls is 1000
def Factorial(n):
    if n == 1:
        return 1
    else :
        return n * Factorial(n -1)

print(Factorial(5))