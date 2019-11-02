def reorganizeString(S):
        """
        :type S: str
        :rtype: str
        """
        c = [0 for _ in range(26)]
        res = ""
        for i in range(len(S)):
            c[ord(S[i]) - ord('a')] += 1
        for i in range(26):
            if c[i] > ((len(S)+1)//2):
                return res
        q = queue.PriorityQueue()
        for i in range(26):
            if c[i] > 0:
                q.put([-a[i],chr(i+ord('a'))])
        while q.qsize() > 1:
            s1 = q.get()
            s2 = q.get()
            res += s1[1]
            res += s2[1]
            if s1[0] < -1:
                s1[0] += 1
                q.put(s1)
            if s2[0] < -1:
                s2[0] += 1
                q.put(s2)
        if q.qsize() > 0:
            res += q.get()[1]
        return res
            
            

print(reorganizeString)



