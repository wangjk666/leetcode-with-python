# 其实就是相当于给出了一些二维数组，找出他们中有重叠的分为一组，找出最小的组数
def findMinArrowShots(points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        points.sort(key = lambda x:x[0])
        points.sort(key = lambda x:x[1])
        last = 0
        counts = 1
        for i in range(1,len(points)):
            if points[i][0] > points[last][1]:
                last = i
                counts += 1
        return counts