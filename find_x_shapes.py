
def find_neighbor_x(input, i, j, visited, result=None):
    if result is None:
        result = []
    visited[i][j] = 1
    result.append((i, j))
    n = len(input)
    m = len(input[0])
    if (i-1) >= 0 and input[i-1][j] == 1 and visited[i-1][j] == 0:
        find_neighbor_x(input, i-1, j, visited, result)
    if (i+1) < n and input[i+1][j] == 1 and visited[i+1][j] == 0:
        find_neighbor_x(input, i+1, j, visited, result)
    if (j-1) >= 0 and input[i][j-1] == 1 and visited[i][j-1] == 0:
        find_neighbor_x(input, i, j-1, visited, result)
    if (j+1) < m and input[i][j+1] == 1 and visited[i][j+1] == 0:
        find_neighbor_x(input, i, j+1, visited, result)
    return result
        
def find(input):
    n = len(input)
    m = len(input[0])
    visited = [[0 for i in range(m)] for j in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if input[i][j] == 1 and visited[i][j] == 0:
                temp = find_neighbor_x(input, i, j, visited)
                result.append(temp)
    print(result)

input = [[0,0,0,1,1,0,1]]
find(input)
