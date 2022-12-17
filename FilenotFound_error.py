"""
with open("text.txt",'r') as f:
print(f.read()) #this file is not present in the directory so it will throw filenotfound error
"""

try:
    with open("text.txt",'r') as f:
        print(f.read())
except FileNotFoundError as f:
    print(f"The given code has {f} error")
    with open("text.txt",'w') as f:
        print(f.write("Hello, I have created a new file"))