def rotate_matrix(a):
    n = len(a)
    m = (n%2) + int(n/2)
    for i in range(m):
        for j in range(i,n-i-1):
            temp = a[i][j]
            a[i][j] = a[(n-j-1)%n][i]
            a[(n-j-1)%n][i] = a[(n-i-1)%n][(n-j-1)%n]
            a[(n-i-1)%n][(n-j-1)%n] = a[j][(n-i-1)%n]
            a[j][(n-i-1)%n] = temp

    for i in a:
        print(i)

matrix1=[[1,2],[3,4]]
rotate_matrix(matrix1)
matrix1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix1=[]
for i in range(1,11):
    matrix1.append([])
    for j in range(1,11):
        matrix1[i-1].append(j + (10*(i-1)))
rotate_matrix(matrix1)
