def findSubstringInWraproundString(p):
        """
        :type p: str
        :rtype: int
        """
        dp = [0 for _ in range(26)]
        dp[ord(p[0]) - ord('a')] = 1
        dpi = 1
        for i in range(1,len(p)):
            if (ord(p[i]) - ord(p[i-1])) == 1 or (ord(p[i-1]) - ord(p[i])) == 25:
                dpi += 1
            else:
                dpi = 1
            dp[ord(p[i])-ord('a')] = max(dpi, dp[ord(p[i]) - ord('a')])
            print(i,dp[ord(p[i])-ord('a')])
        sum = 0
        for i in range(26):
            sum += dp[i]
        return sum
    
print(findSubstringInWraproundString('zab'))

                
