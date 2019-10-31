def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    n = len(triangle)
    dp = triangle[-1]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):  # 从倒数第二层开始网上，变化数字，dp[-1]一开始就用不到了
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    return dp[0]


