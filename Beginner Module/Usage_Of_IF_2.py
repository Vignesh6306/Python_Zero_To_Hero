# Short Hand IF

A = 300
B = 1000

print('A not equals B') if A != B else print('A equals B')

# Nestesd If

if(A<B):
    print('A is less than B')
    if(A%2 == 0):
        print('A is even')
    elif(A%3 == 0):
        print('A is odd')
    else:
        print('Invalid')
else:
    print('A is not less than B')

# Use pass keyword to avoid Identation or line after IF

x = 'hello'
if 'l' in x:
    pass
print('L is present in hello')
