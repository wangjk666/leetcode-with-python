def kClosest(points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        lo,hi = partition(points)
        print(len(lo))
        print(len(hi))
        if len(lo) == K:
            return lo
        elif len(lo) < K:
            return lo + kClosest(hi,K-len(lo))
        else:
            return kClosest(lo,K)


def dis(point):
    return pow(point[0],2) + pow(point[1],2)

def partition(points):
    lo = []
    hi = []
    target = points[0]
    for i in range(len(points)):
        if dis(points[i]) <= dis(target):
            lo.append(points[i])
        else:
            hi.append(points[i])
    return lo,hi
        

points = [[1,3],[-2,2]]
print(kClosest(points,1))