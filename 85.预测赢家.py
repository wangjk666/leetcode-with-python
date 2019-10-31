def PredictTheWinner(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        本例中采用动态规划的算法，动态规划有一个非常典型的特征，就是
        相比于dfs之类的算法，是从后向前看的过程，也就是根据动态规划的
        递推方程，是从后向前，从左向右遍历的。
        """
        l = len(nums)
        maxprofit1 = [[0]*l for _ in range(l)]
        maxprofit2 = [[0]*l for _ in range(l)]
        for i in range(l):
            maxprofit1[i][i] = nums[i]
        for i in range(l-1,-1,-1):
            for j in range(i+1,n):  
                """
                如果在i~j之间选择了i的话，下一轮的收益就会成为后手,而且下一轮在i+1~j选择
                如果选了j的话，下一轮的收益就是后手，下一轮在i~j-1中进行选择
                """
                left = nums[i] + maxprofit2[i+1][j]
                right = nums[j] + maxprofit[i][j-1]
                if left > right:
                    maxprofit1[i][j] = left
                    maxprofit2[i][j] = maxprofit1[i+1][j]
                else:
                    maxprofit1[i][j] = right
                    maxprofit2[i][j] = maxprofit1[i][j-1]
        return maxprofit1[0][n-1] > maxprofit2[0][n-1]

"""
如果dp[i][j]表示在i～j的过程中先手比后手多的收益
def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[0]*n for _ in range(n)]        # 初始化
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = nums[i]        # 当前序列状态为单值，先手比后手收益多的最大值为 nums[i]
                else:
                    dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1]) 
        return (dp[0][n-1] >= 0)
"""