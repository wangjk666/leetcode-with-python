# 找到和为n的k个数的组合
def combinationSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    result = list()
        _combinationSum3(n, 1, list(), result, k)
        return result

    def _combinationSum3(target, index, path, res, k):
        if target == 0 and len(path) == k:
            res.append(path)
            return 

        if path and target < path[-1]:
            return
       
        for i in range(index, 10):
            _combinationSum3(target-i, i + 1, path+[i], res, k)

print(combinationSum3(3,7))
