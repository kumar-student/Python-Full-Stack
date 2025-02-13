# File open
try:
    file = open("sample.txt", "r")
except FileNotFoundError as e:
    print(e)
    
# File read and print
try:
    a = 10
    content = file.read()
    print(content)
    file.close()
except NameError as e:
    print(e)
finally:
    del a
    print("Finally executed")

# print(a)  Give NameError