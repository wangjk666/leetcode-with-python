def smallestRangeII(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    """
    重点是找到一个节点i,0~i-1要减K，i~l要加K
    这操作以后呢，0～i-1里面0最小i-1最大
    i~l里面i最小,l最大
    需要做一个比较找出最大的和最小的
    """
    n=len(A)
        A=sorted(A)
        res=A[n-1]-A[0]
        for i in range(1,n):
            small=min(A[0]+K,A[i]-K)
            large=max(A[i-1]+K,A[n-1]-K)
            res=min(res,large-small)
        return res

    

