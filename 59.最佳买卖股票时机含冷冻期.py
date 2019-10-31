def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 解题的思路是设置一个二维的数组dp,一行有两个元素，分别表示在第i天卖和买的最大的利润
        # sell[i] = max(前一天卖出的收入，表示前一天卖出了今天就什么也不做；前一天买的花销和今天卖出的收入)
        # buy[i]  = max(前一天买的花销，大前天卖的收入-今天买的价格)
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        for i, price in enumerate(prices):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -price
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]) 
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i]) #前天买的今天才能卖
        return dp[i][0] if prices else 0
