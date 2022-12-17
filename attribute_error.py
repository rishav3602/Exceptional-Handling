"""
y = 9
y.append(8) #int object has no attribute as append so its an attribute error. 
print(y)

"""

y = 9
try:
    y.append(6)
    print(y)
except AttributeError as a:
    print(f"The given code has {a} error")
    print("Append attribute is not valid for an integer")
    print(f'The value of y cannot be changes using append method, y= {y}')
