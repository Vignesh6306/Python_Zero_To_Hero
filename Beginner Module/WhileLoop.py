# While Loop : Run until the condition is true

# Example 1
print('Example 1 : ')
i = 0
while i <= 10:
    print(i)
    i += 1

# Example 2
print('Example 2 : ')
A = 0
while A <= 20:
    A += 1
    if A%2==0:
        print(A)

# Example 3 : with using break and continue
print('Example 3 : ')
B = 0
while B <= 20:
    B += 1
    if B %3 == 0:
        continue
    elif B == 10:
        break
    else:
     print(B)


