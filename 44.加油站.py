def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    if sum(gas) < sum(cost):
        return -1
    else:
        res = 0
        station = 0
        for i in range(len(gas)):
            if res + gas[i] - cost[i] < 0:
                station = i + 1
                res = 0
            else:
                res = res + gas[i] - cost[i]
        return station

