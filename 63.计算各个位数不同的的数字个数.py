def countNumbersWithUniqueDigits(n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        dp = [0] * n
        dp[0] = 10
        for i in range(1, n):
            re = 9
            for j in range(i):
                re *= (9-j)
            dp[i] = dp[i-1] + re
        return dp[n-1]


print(countNumbersWithUniqueDigits(2))