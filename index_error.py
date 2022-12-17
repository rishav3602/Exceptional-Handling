"""
# INDEX ERROR

myList = [1,2,3,4,5,6,7,8]
print(myList[10]) #10th index is not present in the given list it will throw index error.

"""

# HANDLING 


myList = [1,2,3,4,5,6,7,8]
try:
    print(myList[10])
except IndexError:
    print("List index is out of range")
    for i in myList:
        index = i-1
    print(f"The last index of the given list is {index}.")


try:
    for i in range(len(myList)+1):
        index = i
        print(myList[i])

except IndexError:
    print(f"your list have just {index} index")