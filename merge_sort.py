
def mergesort(arr, l, r):
    if l < r:
        mid = int((l+r)/2)
        mergesort(arr, l, mid)
        mergesort(arr, mid+1, r)
        merge(arr, l, mid, r)

def merge(arr, l, m, r):
    i = l
    j = m + 1
    while(i<=m and j<=r):
        if arr[i] > arr[j]:
            temp = arr[j]
            del arr[j]
            arr.insert(i, temp)
            j = j+1
        else:
            i = i + 1

input = [7,1,3,10,1]
n = len(input)
mergesort(input, 0, n-1)

print(input)
