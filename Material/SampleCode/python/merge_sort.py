# Devide and conquer
# 1. Devide into sub arrays
# 2. Compare and merge arrays
# 3. Repeate 1 and 2 for all sub arrays

def merge(left, right):
    # if left array is empty nothing to merge
    # you can return right array 
    
    # if right array is empty nothing to merge
    # you can return left array

    # traverse through length if left+right arrays
    # with left ang right indexes

    # If left array element <= right array element
    # insert left array element into result array
    # increase left index

    # If right array element < left array element
    # Insert right array element into result array
    # increse right index

    # If you reached at the end of left or right array
    # insert other array elements to the result
    pass

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    midpoint = len(arr)//2

    return merge(
        left=merge_sort(arr[:midpoint]),
        right=merge_sort(arr[midpoint:])
    )