x = 10 
y = "i"

try:
    print("I want to go in the nested block")
    try:
        print("This is my nested block")
        print(x/int(y))
    except ValueError as v:
        print("This is my value error")
        print(v)
except ZeroDivisionError as z:
    print("Trying to divide by zero")
    print(z)