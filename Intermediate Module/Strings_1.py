# Strings = Sequence of Character surrounded by single of double quotes
S = "Welcome to Python"
print(S)

# For Multi-Line String Use triple quotes
M = '''
Hello!
Are you feeling excited
to learn python.
Then you are welcome 
'''
print(M)

#Use len keyword to know the length of the Strings
print(len(S))
print(len(M))

#String indexing : Variable[index_Value] -> Index value usually starts at 0.
A = "Hello World"
print(A[0], A[1], A[2], A[3], A[4], sep=',')

# Method - 2 : Variable[Start : End-1]
print(A[6 : 11])
print(A[ : 5])
print(A[6 : ])

# Method - 3 : Variable[Start : End : Steps] -> Steps default starts with 1.
# Negative Indexing Usually starts at -1.

print(S[:  : 1])
print(S[-1: -15: -2])



