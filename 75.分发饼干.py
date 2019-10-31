# 输入一个胃口数组和一个饼干大小的数组，让更多的胃口得到满足
def findContentChildren(g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        len1=len(g)
        len2=len(s)
        i=0
        j=0
        num=0
        while i<len1 and j<len2:
            if g[i]<=s[j]:
                num+=1
                i+=1
            j+=1
        return num
