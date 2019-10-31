def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    if m < 1 or n < 1:
        return 0
    path = [[0]*n]*m
    for i in range(n):
        path[0][i] = 1
    for j in range(m):
        path[j][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            path[i][j] = path[i-1][j] + path[i][j-1]
    return path[m-1][n-1]
