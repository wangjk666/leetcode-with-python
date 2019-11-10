def helper(visited, lookup, maxChoosableInteger, total):
    if visited in lookup:
        return lookup[visited]
    for i in  range(maxChoosableInteger):
        cur = 1<<i;
        if cur&visited == 0:
            if total <= i+1 or helper(visited|cur, lookup, maxChoosableInteger, total-(i+1)) == False :
                lookup[visited] = True
                return True
    lookup[visited] = False
    return False



def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if maxChoosableInteger >= desiredTotal:
        return True
    if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal:
        return False
    if maxChoosableInteger*(maxChoosableInteger+1)/2 == desiredTotal:
        return maxChoosableInteger%2
    mem = {}
    return helper(0, mem, maxChoosableInteger, desiredTotal)

print(canIWin(10,11))