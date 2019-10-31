def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    row_index = []
    col_index = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                row_index.append(row)
                col_index.append(col)

    for row in row_index:
        matrix[row] = [0] * cols

    for col in col_index:
        for row in range(rows):
            matrix[row][col] = 0


