"""
输入: "112358"
输出: true 
解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"""
def isAdditiveNumber(num):
        """
        :type num: str
        :rtype: bool
        """
        # junge函数的参数分别是a、b为int型的整数，s是整个包含a、b的字符串
        # 如果a、b、a+b拼接成的字符串就是s那么直接返回true
        # 如果拼接成的字符串的长度大于s的长度，那么直接返回false
        # 否则返回junge(b,a+b,s[a之后的字符串])
        def junge(a,b,s):
            c=a+b
            temp=str(a)+str(b)+str(c)
            if s==temp:
                return True
            elif len(s)<len(temp):
                return False
            if s[:len(temp)]==temp:
                return junge(b,c,s[len(str(a)):])
            else:
                return False
 
 
        for i in range(1,len(num)//2+1):
            a=int(num[:i])
            j=1
            while j+i<(len(num)+i)//2+1:
                b=int(num[i:i+j])
                if junge(a,b,num):
                    return True
                j+=1
 
        return False



