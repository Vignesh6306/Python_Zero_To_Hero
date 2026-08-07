# Arithmetic Operators

print("Arrithmetic Operators")
A = 10
B = 3
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B) # Return the remainder
print(A**B) # Return the exponent of A^B
print(A//B) # Return the Quotient without float
print(sep = '\n')

# Assignment Operators

print("Assignment Operators")
A += 5 # A = A+5
print(A)
A -= 10 # A = A-10
print(A)
A *= 2 # A = A*2
print(A)
A /= 5 # A = A/5
print(A)
print(sep = '\n')

# Comparison Operators

print("Comparison Operators")
print(A == B) # Check Both the values are same
print(A != B) # Check A is not B
print(A > B) # Check A is greater then B
print(B < A) # Check B is lesser than A
print(A <= B) # LessThan or equal to B
print(B >= A) # GreaterThan or eqaul to A
print(sep = '\n')

# Logical Operators

print("Logical Operators")
print(A==B and A < B) # Check whether the both values are true
print(A!=B or A > B) # Check any One value is true from both
print(not(A<=10)) # Return opposite
print(sep = '\n')

# Identity Operators

print("Identity Operators")
C = [10,20,30]
D = [10,20,30]
E = C
print(C is D) # Even though both the variables has the same values. But allocated different memory for the both
print(C is E)
print(D is not E)
print(sep = '\n')

# Membership Operators

print("Membership Operators")
X = "Hello World"
Y = "Hello"
print(X in Y)
print('H' in X) # check wether the Character is in the defined String
print('z' not in X) # check wether the Character is not in the defined String
print(sep = '\n')






