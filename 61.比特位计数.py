"""
考虑二进制数的规律。
[000,001,010,011,100,101,110,111]，
分别对应[0,1,2,3,4,5,6,7]。从上述二进制数可以看出来，
4-7的二进制数既是对0-3的二进制数的最高位从0变成1，也就是说后面的二进制数都是在之前所有二进制的最高位加一位1。
"""
def countBits(num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [""] * num
        dp[0] = '0'
        for i in range(1,len(dp)):
            if dp[i-1][0] == '0':
                dp[i] = dp[i-1].replace('0','1',1)
                print(dp[i])
            else:
                dp[i] = str(1) + dp[i-1].replace('1','0',1)
                print(dp[i])
        l = []
        for i in range(len(dp)):
            l.append(dp[i].count('1'))


print(countBits(5))
