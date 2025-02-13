arr = [1, 22, 33, 44, 55, 66, 77, 88, 99, 100]

e = int(input("Give a number: "))

for i in range(len(arr)):
    if arr[i] == e:
        print("Found at :", i)