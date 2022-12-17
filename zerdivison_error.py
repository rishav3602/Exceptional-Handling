"""
a = int(input("Enter your number :"))
b = int(input("Enter your number :"))
c = a/b #will throw an error if divided by zero
print(c)
"""
#handling

try:
    a = int(input("Enter your number :"))
    b = int(input("Enter your number :"))
    c = a/b 
    print(c)
except ZeroDivisionError as z :
    print(f"this code has {z} error")
    print("Divison by zero is not possible ")
except ValueError as v :
    print("Entered value is wrong")