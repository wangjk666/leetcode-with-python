def existbfs(i, j, visited, cur, board, word):
    if cur == len(word):
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
        return False
    visited[i][j] = True
    result = existbfs(i + i, j, visited, cur + 1, board, word) or \
             existbfs(i - 1, j, visited, cur + 1, board, word) or \
             existbfs(i, j + 1, visited, cur + 1, board, word) or \
             existbfs(i, j - 1, visited, cur + 1, board, word)

    # 下一句是关键，搜索完当前的所有方向之后将当前的访问器设为false，实现一种回溯的效果
    visited[i][j] = False
    return result


def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    visited = [[False for j in range(range(len(board[0])))] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):

            # 这种bfs、dfs的遍历，只要找到一个入口判别是为为真即可，因为这是一个递归函数，
            # 当然首先要遍历所有board找到正确的入口
            if existbfs(i, j, visited, 0, board, word):
                return True
    return False
