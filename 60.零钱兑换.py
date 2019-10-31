def coinChange(coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        re = []
        dfs(coins,amount,0,0,re)
        if len(re) == 0:
            return -1
        else:
            Min = 10000
            for i in range(len(re)):
                Min = min(Min,re[i])
            return Min


def dfs(coins,amount,i,counts,re):
    if amount == 0:
        re.append(counts)
        return
    if i >= len(coins):
        return
    l = amount // coins[i]
    for j in range(l+1):
        dfs(coins,amount-j*coins[i],i+1,counts+j,re)


"""
动态规划。用dp[i] 表示组成 i 元所需要的最小硬币数。
显然对于coins数组里的所有元素j，所有的dp[j] = 1。
以样例输入一为例：
对于其他的dp[i] = 1 + min(dp[i - 1], dp[i - 2], dp[i - 5])
即求11元的答案可以转化为： 1个一元硬币 + 10元答案 或者 1个两元硬币 + 9元答案 或者1个五元硬币 + 6元答案。
所以dp[i] = 1 + min(dp[i - j]) for j in coins
"""

def coinChange(coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = list()
        max_int = 2 << 31
        
        for i in range(amount + 1):
            if i not in coins:
                dp.append(max_int)
            else:
                dp.append(1)
        
        for i in range(amount + 1):
            if i not in coins:
                for j in coins:
                    if i - j > 0:
                        dp[i] = min(dp[i - j] + 1, dp[i])
            
        return dp[amount] if dp[amount] != max_int else -1

coins = [1,2,5]
amounts = 11
print(coinChange(coins,amounts))