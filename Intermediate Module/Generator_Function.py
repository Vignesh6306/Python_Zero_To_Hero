# Example 1

def gen_1():
    yield 1
    yield 2

for x in gen_1():
    print(x, 'The number')
    print(x, 'Points the next number')
    print('==========================')

# Example 2

print(sep = '/n')
def fibo(limit):
    a, b = 0, 1

    while a <= limit:
        yield a
        a, b = b, a+b

for x in fibo(100):
    print(x)