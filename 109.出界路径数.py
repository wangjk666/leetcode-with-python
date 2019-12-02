def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        # 增加网格边界，初始值设为1。 dp[o][p][q]表示网格在(p-1, q-1)位置时，讲过N此移动出边界的次数
        dp = [[[0 for q in range(n+2)] for p in range(m+2)] for o in range(N+1)]
        for o in range(N+1):
            for p in range(m+2):
                for q in range(n+2):
                    if p == 0 or p == m+1 or q == 0 or q == n+1:
                        dp[o][p][q] = 1
        
        for o in range(1, N+1):
            for p in range(1, m+1):
                for q in range(1, n+1):
                    dp[o][p][q] = dp[o-1][p-1][q] + dp[o-1][p+1][q] + dp[o-1][p][q-1] + dp[o-1][p][q+1]
        
        return dp[N][i+1][j+1] % (10**9 + 7)
