import math
def rotate_matrix(a, n):
    for j1 in range(n):
        for i1 in range(n):
            t1 = a[n*(n-i1-1)+j1]
            print(t1, end=" ")
import pdb; pdb.set_trace()
matrix1=[1,2,3,4]
rotate_matrix(matrix1, 2)
matrix1 = [i for i in range(1,10)]
rotate_matrix(matrix1, 3)
matrix1=[i for i in range(1,17)]
rotate_matrix(matrix1, 4)
