def div (*args):
    try:
        x= int(input("Enter your number : "))
        y= int(input("Enter your number : "))
        s = x/y
        print(s) 
    except ZeroDivisionError as z:
        print("Divison by zero is not possible")
        print(z)
    else:
        return("This is from else block")
    finally:
        print("Finally execution is done.")

z = div()