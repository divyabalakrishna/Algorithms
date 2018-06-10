# Implementation of selection sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = 9999999999999
        pos = -1
        for j in range(i, n):
            if arr[j] < min:
                min = arr[j]
                pos = j

        del arr[pos]
        arr.insert(i, min)

arr = [3, 7, 9, 1, 4, 2, 1, 10, 8]

selection_sort(arr)

print(arr)
