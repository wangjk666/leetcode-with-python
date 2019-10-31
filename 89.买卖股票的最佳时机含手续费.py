def maxProfit(prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        """
        方法是初始化两个list,
        sell[i]表示今天卖出状态下最大的收益，
        hold[i]表示今天持有股票状态下最大的收益，
        sell[i]对应两种情况,第一种是今天刚刚sell,就是hold[i-1]+prices[i]-fee,第二种就是之前就sell今天什么也没做,就是sell[i-1];
        hold[i]对应两种情况，第一种是今天刚刚买到,就是sell[i-1]-prices[i],第二种是之前就hold今天什么也没做,就是hold[i-1]
        """
        l = len(prices)
        sell = [0 for _ in range(l)]
        hold = [0 for _ in range(l)]
        sell[0] = 0
        hold[0] = -prices[0]
        for i in range(1,l):
            sell[i] = max(hold[i-1]+prices[i]-fee,sell[i-1])
            hold[i] = max(sell[i-1]-prices[i],hold[i-1])
        return sell[l-1]