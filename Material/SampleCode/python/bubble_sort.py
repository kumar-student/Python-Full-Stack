def bubble_sort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(0, l-i-1):
            print(i, j)
            if arr[j] > arr[j+1]:
                swap(arr, i, j)

def swap(arr, i, j):
    print("Swap: ", arr[i], arr[j])
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

arr = [64, 34, 25, 12, 22, 11, 90]
print("input: ", arr)
bubble_sort(arr)
print("output: ", arr)
