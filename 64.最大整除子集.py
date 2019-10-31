# 题目的要求是给定一个数组，返回一个相互都能整除的最大子数组
# 动态规划的第一步不应该思考怎么划分的问题，而应该思考dp数组代表什么含义的问题
# 现在来看，dp数组一般可以代表的就是以数组当前元素为结尾的解
# 然后判断当前为结尾的解和之前的解有什么关系，这个一般是依靠问题的描述来决定的
# 比如这一题，dp[i] = max(dp[a1],dp[a2]..)+1，其中nums[ai]可以整除nums[i]
# 用一个index数组的作用是可以记录目前取的最大的位置在哪里


def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        N = len(nums)
        nums.sort()
        dp = [0] * N 
        parent = [0] * N
        mx = 0
        mx_index = -1
        for i in range(N):
            for j in range(i - 1, -1 , -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > mx:
                        mx = dp[i]
                        mx_index = i
        res = list()
        for k in range(mx + 1):
            res.append(nums[mx_index])
            mx_index = parent[mx_index]
        return res[::-1]
        # list[start:end:step]
