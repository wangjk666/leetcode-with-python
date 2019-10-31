# 题目描述是给定n，找到最少的平方数使得他们的和等于n
import math
def ispf(n):
    tmp = math.sqrt(n)
    tmp = int(tmp)
    if tmp * tmp == n:
        return True
    else:
        return False

def dfs(n,counts,res):
    if n == 0:
        res.append(counts)
        return
    if n < 0:
        return
    for i in range(n,0,-1):
        if ispf(i):
            dfs(n-i,counts+1,res)


def findMin(alist):
    if alist is None:
        return 0
    if len(alist) == 1:
        return alist[0]
    findMin = alist[0];
    for i in alist:
        if i < findMin:
            findMin = i
    return findMin


def numSquares(n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        dfs(n,0,res)
        return findMin(res)



# 以上的时间复杂度在leetcdoe上不行，换为动态规划
#维护一个长度为n+1的数组dp，dp[i]表示i的最小完全平方数组成个数；
"""
for i in 1~n：
（1）如果i为完全平方数，有dp[i] = 1
（2）如果i不为完全平方数，dp[i] = min(dp[j*j] + dp[i - j*j]) for j = 1~sqrt(n)
"""

int numSquares(int n) {
        vector<int> v(n+1,n);
        v[0]=0;
        for(int i=1;i<=n;i++){
            for(int k=1;k*k<=i;k++){
                    v[i]=min(v[i],v[i-k*k]+1);
                }
        }
        return v[n];
    }


num = 12
print(numSquares(num))

