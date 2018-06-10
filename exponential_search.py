
# using exponential searc algorithm, search for a given element

def binary_search(arr, start, end, ele):
    if start > end:
        return -1

    mid = int((start + end) / 2)
    if arr[mid] == ele:
        return mid
    elif ele > arr[mid]:
        return binary_search(arr, mid+1, end, ele)
    else:
        return binary_search(arr, start, mid-1, ele)

    return -1

def exp_search(arr, ele):
    # ele: element to be searched in arr
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == ele:
            return i
        if arr[i] > ele:
            pos = binary_search(arr, int(i/2), i, ele)
            return pos

        if i == 0:
            i = 1
        else:
            i = i * 2

    return -1

arr = [x for x in range(1, 11)]

print(exp_search(arr, 5))
