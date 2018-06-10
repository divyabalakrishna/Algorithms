# sort using insert sort algorithm in increasing order

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        for j in range(i):
            if temp < arr[j]:
                del arr[i]
                arr.insert(j, temp)
                break

arr = [1, 7, 9, 1, 4, 2, 10]

insertion_sort(arr)
print(arr)
