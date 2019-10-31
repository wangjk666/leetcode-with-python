def leastInterval(tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        m=len(tasks)
        tmp=[0 for i in range(26)]
        for i in range(m):
            tmp[ord(tasks[i])-ord('A')]+=1
        tmp.sort()
        val=tmp[25]
        count=0
        i=25
        while val==tmp[i] and i>=0:
            count+=1
            i-=1
        res=(n+1)*(val-1)+count
        return max(res,m)




print(leastInterval(["A","A","A","B","B","B"],2))
# 解题的思路是这样的，首先统计每个字符的出现的次数并排序，找到出现次数最多的那个字符及其数量
# 然后比如说他出现了var次，那么一定至少需要var组，每组有n+1个
# 最后一组不需要，可能站不满
# 我们需要了解的就是如果前面的var-1组其实不需要关心，因为总是需要的
# 我们需要关心的就是最后一组的
# 也即是我们需要知道哪些变量是前面的var-1组分配不完的，就一定是出现的次数也是var的那些统计一下就行
        
        



