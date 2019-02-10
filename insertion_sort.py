# sort using insert sort algorithm in increasing order

def insertion_sort(arr):
    n = len(arr)

    for j in range(1, n):
        i = j - 1
        key = arr[j]
        while key < arr[i] and i >= 0:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key
    return arr
            
arr = [11, 7, 9, 1, 4, 2, 1, 10]

insertion_sort(arr)
print(arr)
