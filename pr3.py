try:
    num = int(input("Enter your number : "))
    assert num%2 == 0
    print("The given number is even")
except AssertionError:
    print("The given number is odd")
else:
    try:
        r = 1/num
        print(f"The reciprocal of the given number is : {r}")
    except ZeroDivisionError:
        print("Divison by zero is not allowed. ")