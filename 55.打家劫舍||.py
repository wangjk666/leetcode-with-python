def rob(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        res1 = dp(nums[1:])
        res2 = dp(nums[:-1])
        return max(res1, res2)
 
 
    def dp(inputs):
        dp = [0 for _ in range(len(inputs)+1)]
        dp[1] = inputs[0]
        for i in range(2, len(inputs)+1):
            dp[i] = max(dp[i-1], dp[i-2]+inputs[i-1])
        return dp[-1]



