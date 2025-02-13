# from random import randint

def quicksort_recursion(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    less = []
    equal = []
    great = []

    for i in arr:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            great.append(i)
        elif i == pivot:
            equal.append(i)
    return quicksort_recursion(less) + equal + quicksort_recursion(great)

arr = [7, 6, 9, 5, 8, 7, 3, 2, 1]
print("Input: ", arr)
print("Output: ", quicksort_recursion(arr))