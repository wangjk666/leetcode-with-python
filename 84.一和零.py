def findMaxForm(strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        strs.sort(key = lambda x: len(x))
        re = []
        dfs(strs,0,m,n,[],re)
        maxlen = 0
        for i in range(len(re)):
            maxlen = max(maxlen,len(re[i]))
        return maxlen

def dfs(strs,i,mleft,nleft,l,re):
    if mleft < 0 or nleft < 0:
        return
    if (mleft==0 and nleft==0) or i >= len(strs):
        re.append(l)
        return
    ones, zeros = 0, 0
    for k in range(len(strs[i])):
        if strs[i][k] == '0':
            zeros += 1
        else:
            ones += 1
    dfs(strs,i+1,mleft-ones,nleft-zeros,l+[i],re)
    dfs(strs,i+1,mleft,nleft,l,re)    
    
def findmax(strs,m,n):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for str in strs:
        ones, zeros = 0, 0
        for s in str:
            if s == '0':
                zeros += 1
            else:
                ones += 1
        for i in range(m,zeros-1,-1):
            for j in range(n+1,ones-1,-1):
                dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
    return dp[m][n]

l = ["10","0","1"]
m = 1
n = 1
print(findMaxForm(l,m,n))
    

    
