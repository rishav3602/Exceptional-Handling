"""

x = 8
y = 5
assert y!=5, "Invalid operation" #if assert statement is not true it will throw assertion error
print(x/y)

"""


try:
    x = 8
    y = 5
    assert y!=5, "Invalid Operation "
except AssertionError as a:
    print(f"your code has {a} error ")
    print(x/y)
