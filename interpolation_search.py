# code to search for an element using interpolation search

def interpolation_search(arr, ele):
    n = len(arr)

    low = 0
    high = n - 1
    while low <= high:
        pos = low + ((x - arr[low]) * (high - low) / (arr[high] - arr[low]))
        pos = int(pos)
        if arr[pos] == ele:
            return pos

        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
 
x = 1
index = interpolation_search(arr, x)
 
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")
