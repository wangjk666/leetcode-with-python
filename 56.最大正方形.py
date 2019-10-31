def maximalSquare(matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        """
        dp[i][j]表示以第i行第j列为右下角所能构成的最大正方形边长, 则递推式为: 
        dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        """
        row = len(matrix)
        if row < 1:
            return 0
        col = len(matrix[0])
        Max = 0        
        dp = [[0 for _ in range(col+1)]for _ in range(row+1)]
        
        for i in range(1,row+1):
            for j in range(1,col+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = 1 + int(min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]))
                    Max = max(Max,dp[i][j])
        return Max ** 2

