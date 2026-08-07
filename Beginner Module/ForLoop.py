# For loops : Run until the defined condition is true

# Example 1
print('Example 1 : ')
l1 = [1,2,3,4,5]
print(type(l1))
for i in l1:
    print(i * 10)

# Example 2
print('Example 2 : ')
for j in l1:
    if j %2 == 0:
        continue
    elif j == 6:
        break
    print(j)

# Example 3
print('Example 3 : ')
A = [10,20,30]
B = ['Car','Bike','Cycle']
for i in A:
    for j in B:
        print(i,j)

# Example 4 with using range

# range(Start)
for x in range(5):
    print(x)

# range(Start , End)
for y in range(0,11):
    print(y)

# range (Start, End, Steps)
for z in range(0,10,2):
    print(z)


