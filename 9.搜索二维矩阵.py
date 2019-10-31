def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if matrix == [] or matrix == [[]]:
        return False
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                return False
            else:
                if i == m - 1 and j == n - 1:
                    return False