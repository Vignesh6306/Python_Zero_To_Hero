# Single way Selection

price = 500
charge = 50

if price >= 300:
    charge = 0

Total = price + charge
print(Total)

# Two way Selection

Discount = 40
if Total >= 500:
    Total -= Discount
else:
    Discount = 0

print(Total)

# Three way Selection

A = 10

if(A % 2 == 0):
    print('Even')
elif(A % 3 == 0):
    print('Odd')
else:
    print('Invalid Input')
