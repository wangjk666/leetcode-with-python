# 从一个数中移调k位之后最小的数
# 如果剩下的第一位是0就去掉
def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return "0"
        i = 0
        while i < len(num) - 1 and k > 0:#开始搜索
            if(int(num[i])>int(num[i+1])):#如果有一位数字大于下一位，那么将这一位删除
                num = num[0:i]+num[i+1:]
                if i > 0: i -= 1
                k -= 1
            else: i += 1
        # 下面这句话就是有种情况这个数字递增的，所以找不到一个去掉的，就直接取其len(nums)-k位
        num = num[:len(num)-k]
        return str(int(num))