# 输入一个n*2的数组，输出从中去掉几个二维的之后可以让剩下的无重叠
def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key = lambda x:x[0])
    intervals.sort(key = lambda x:x[1])
    last = 0
    new = []
    new.append(intervals[0])
    for i in range(last,len(intervals)):
        if intervals[i][0] >= intervals[last][1]:
            last = i
            new.append(intervals[i])
    return len(intervals)-len(new)


ls = [ [1,2], [2,3], [3,4], [1,3] ]
print(eraseOverlapIntervals(ls))



