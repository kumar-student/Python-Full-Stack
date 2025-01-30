def binary_search(arr, x, start, end):
    while start <= end:
        mid = (start+end)//2
        
        if arr[mid] == x:
            return mid
        
        if arr[mid] < x:
            start = mid + 1
        
        if arr[mid] > x:
            end = mid -1
    
    return None


arr = [3, 4, 5, 6, 7, 8, 9]
x = 7
res = binary_search(arr, x, 0, len(arr)-1)
if res != None:
    print("Found at: ", res)
else:
    print(res)
