def linear_search(arr, target):
    # Your code here
    if not arr:
        return -1
    else: 
        for i in range(len(arr)):
            if arr[i] == target:
                return i
            elif i == len(arr) - 1:
                return -1
            i += 1
    


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here


    return -1  # not found
