import Prog_For_Import as p
from Prog_For_Import import welcome, Table

p.welcome()

n = int(input("Enter the number to know the multipes of (1-10) : "))
print(p.Table(n))
