# Sort arry using bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [3, 7, 9, 1, 4, 2, 10]
bubble_sort(arr)
print(arr)
