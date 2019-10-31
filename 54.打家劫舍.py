# 题目描述是如果偷相邻房间会触发报警器
def rob(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        else:
            dp = [0] * len(num)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return dp[len(nums)-1]

nums = [1,2,3,1]
print(rob(nums))