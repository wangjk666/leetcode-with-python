from math import sqrt
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    l = 1
    r = x
    while l <= x:
        res = (l+r) // 2
        s = res**2
        if s <= x < (res+1)**2:
            return res
        if s < x:
            l = res
        if s > x:
            r = res


