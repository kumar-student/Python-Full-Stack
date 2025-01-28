# File open
try:
    file = open("sample.txt", "r")
except FileNotFoundError as e:
    print(e)
    
# File read and print
try:
    content = file.read()
    print(content)
    file.close()
except Exception as e:
    print(e)
finally:
    print("Finally executed")