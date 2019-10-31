# 给定假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。
# 重新排序的目的是使得这个序列符合（h,k)
# 做法是先根据身高从高到低排序,如果是身高相同的k小的排在前面
# 然后根据k进行插入，k是几就插入到哪个位置，矮的后来插因为不影响k

def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda (h, k): (-h, k))
        res = []
        for p in people:
            # insert就是第一个是插入的位置，第二个是对象
            res.insert(p[1],p)
        return res