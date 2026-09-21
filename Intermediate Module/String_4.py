S = "Welcome to Python"
S2 = 'A B C D E'
S3 = ['H', 'E', 'L', 'L', 'O']

# Split : Used to Separate the inputs with the defined items
print(S.split())
print(S.split('o'))
print(S2.split(' ',2))

# Join : Used to Merge the inputs with the defined items
print(','.join(S3))
print('_'.join(S3))

# Find & Index : Both produce same outputs. Which produce the starting index of the defined items
print(S.find('e'))
print(S.rfind('e'))
print(S.index('o'))
print(S.rindex('o'))

# Concatenation : Adding 2 String Using + symbol
Text_1 = 'Hello'
Text_2 = 'Hi welcome'
Text_3 = 20
T = Text_1 + '_' + Text_2
print(T)
T2 = Text_1 +' '+ str(Text_3)
print(T2)

# Format : Adds the content in the placeholder {}
Name = input("Enter your name : ")
Age = int(input("Enter your age : "))
F = 'Hi {} welcome to python and good start for your age of{}'
print(F.format(Name, Age))



