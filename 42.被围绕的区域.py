def ifconnectedtobound(board, i, j):
    if i-1 == 0 and board[i-1][j] == 'O':
        return True
    elif i+1 == len(board)-1 and board[i+1][j] == 'O':
        return True
    elif j-1 == 0 and board[i][j-1] == 'O':
        return True
    elif j+1 == len(board[0])-1 and board[i][j+1] == 'O':
        return True
    else:
        return False

def solve(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])
    for i in range(1, m-1):
        for j in range(1, n-1):
            if board[i][j] == 'O' and not ifconnectedtobound(board, i, j):
                board[i][j] == 'X'
            else:
                continue
    return board


