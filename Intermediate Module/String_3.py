Str = "Hello Welcome 2 Python123___"

# dir : To see the dunder and predefined methods
print(dir(Str))

# To check Alpha-Numeric use isalnum, isalpha & isnumeric
print(Str.isalnum())

# To check Upper or Lower case use islower & isupper
print(Str.isupper())

# To replace any char or sequence use replace('')
Str2 = Str.replace('o', 'oo')
print(Str2)
print(Str2.istitle())

# To remove the unwanted space or unwanted thing use strip(), lstrip() and rstrip()
print(Str2.strip('_'))
print(Str2.lstrip('_'))
print(Str2.rstrip('_'))

# To verify anything start with end with
print(Str.startswith('Hello'))
print(Str2.endswith("___"))
