# 思路是先进行横向翻转，再进行纵向翻转
# 横向翻转的话就是如果A[i][0]=0就将这一行翻转，也就是保证第一个元素一定是1
# 纵向翻转的话就是让每一列尽可能多的1

def matrixScore(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """
    res=0
        m=len(A)
        n=len(A[0])
        for i in range(0,m):
            if A[i][0]==0:
                for j in range(n):
                    A[i][j] = 1-A[i][j]
        for j in range(1,n):
            count=0
            for i in range(0,m):
                if A[i][j]==1:
                    count += 1
            if count<=m//2:
                for i in range(0,m):
                    A[i][j] = 1-A[i][j]
        for i in range(0,m):
            for j in range(n):
                res += A[i][j]*(2**(n-1-j))
        return res


print(matrixScore(
    [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
))

