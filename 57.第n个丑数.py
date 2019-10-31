"""
动态规划思想。后面的丑数一定是由前面的丑数乘以2、3或5得到。
所以第n个丑数一定是由前n-1个数中的某3个丑数（分别记为index2、
index3、index5）分别乘以2、3或者5得到的数中的最小数，
index2，index3，index5有个特点，即分别乘以2、3、5得到的数
一定含有比第n-1个丑数大（可利用反证法：否则第n-1个丑数就是它们
当中的一个）最小丑数，即第n个丑数由u[index2]*2、u[index3]*3、
u[index5]*5中的最小数得出。让它们分别和第n个丑数比较，
若和第n个丑数相等，则更新它们的值。
注：一次最少更新一个值（如遇到第n个丑数是6时，index2和index3都要更新）。

"""

def nthUglyNumber(n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return False
        t1 = 0
        t2 = 0
        t3 = 0
        res = [1]
        while len(res) < n:
            res.append(min(res[t1]*2, res[t2]*3, res[t3]*5))
            if res[-1] == res[t1]*2:
                t1 += 1
            if res[-1] == res[t2]*3:
                t2 += 1
            if res[-1] == res[t3]*5:
                t3 += 1
        return res[-1]