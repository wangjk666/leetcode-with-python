def advantageCount(A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        l = len(A)
        ans = [0 for _ in range(l)]
        b = sorted(list(range(l)), key=(lambda x: B[x]))
        a = sorted(A)
        s, e = 0, l - 1
        for i in range(l):
            if a[i] > B[b[s]]:
                ans[b[s]] = a[i]
                s += 1
            else:
                ans[b[e]] = a[i]
                e -= 1
        return ans

print(advantageCount([2,7,11,15],[1,10,4,11]))