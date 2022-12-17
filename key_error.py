"""
mydict= {"name":"Rishav","course":"Data Science"}
print(mydict["age"]) #age key is not present in the dictonary
"""

mydict= {"name":"Rishav","course":"Data Science"}

try:
    print(mydict["age"])
except KeyError:
    print("The age key is not present in the given dictonary")
    print(f"Only these keys are present in dictonary : {mydict.keys()}")
