def func():
    flag = True
    while flag:
        try:
            a = int(input("Enter a value of a : "))
            if type(a) == int:
                print(a)
                flag = False
        except ValueError as v :
            print("you have enter a wrong value")
            print(v)
        
func()
