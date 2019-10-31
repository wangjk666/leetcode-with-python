def dfs(re,n, temp,k):
    if len(temp) == k:
        re.append(temp)
        return
    for i in range(n):
        if len(temp) != 0 and i+1 <= temp[len(temp)-1]:
            continue
        temp.append(i+1)
        dfs(re, n, temp, k)
        temp.pop()


def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    temp = []
    re = [[]]
    dfs(re, n, temp, k)
    return re

