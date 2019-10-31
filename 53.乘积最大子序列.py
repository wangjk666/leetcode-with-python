 def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 因为会有负数的出现，所以会前i个的最大乘积子序列求i+1个乘积子序列的时候，分为以下三种情况：
        # 1. A[i+1] * output(i)，也就是A[i+1]是个正数，前i个的结果也是个负数
        # 2. A[i+1] * 前i个子序列中最小的，比如A[i+1] 是个负数的时候
        # 3. A[i+1]，这样的情况比如 [-3,6],求出来的前i个的输出是一个负数，但是A[i]是个正数
        if len(nums) == 1:
            return nums[0]
        posmax, negmax = 0,0
        # posmax, negmax分别记录着正的最大和负的最大
        result = nums[0]
        for i in range(len(nums)):
            tempposmax = posmax
            tempnegmax = negmax
            posmax = max(nums[i],max(nums[i]*tempposmax,nums[i]*tempnegmax))
            negmax = min(nums[i],min(nums[i]*tempposmax,nums[i]*tempnegmax))
            result=max(result,posmax)
        return result
