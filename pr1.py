import sys

myList = ['a',0,2]
for items in myList:
    try:
        print(f"The item in myList is : {items}")
        r = 1/items
        print(r)
        break
    except:
        print("oops",sys.exc_info()[0],"occured")
        print("next item")

print(f"The value of reciprocal of items in list is : {r}")

