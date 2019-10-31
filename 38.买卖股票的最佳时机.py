def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit, min_price = 0, float("inf")
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
