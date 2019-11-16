def getMaximumGold(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        m, n = len(grid), len(grid[0])
        visited = set()
        res = 0
        
        def dfs(x0, y0, tmp):
            res = max(res, tmp)
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] != 0:
                    visited.add((x, y))
                    dfs(x, y, tmp + grid[x][y])
                    visited.remove((x, y))
                    
        for i in range(m):
            for j in range(n):
                visited.add((i, j))
                dfs(i, j, grid[i][j])
                visited.remove((i, j))
        return res


print(getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))