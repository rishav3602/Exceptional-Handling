def div (x,y):
    try:
        d = x/y
        return(d)
    except ZeroDivisionError as z :
        print("Number cannot be divided by zero")
        return z 

print(div(10,2))
print(div(10,5))
print(div(10,0))
