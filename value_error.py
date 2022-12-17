import math
"""
a = - 400
root_a = math.sqrt(a) #root of negative integer cannot be determined
print(root_a)
"""
try:
    a = -400
    root_a = math.sqrt(a)
    print(root_a)

except ValueError:
    a = -a
    root_a = math.sqrt(a)
    print(root_a)