# Lambda Function : simple function. It have many Parameter but with one expression

def f(x, y):
    z = x + y
    print(z)

print(f(10,20))

# to avoid too much of steps to define a function like the above. We can use Lambda function

x = lambda a, b, z : a+b

print(x(40,60, 0))
