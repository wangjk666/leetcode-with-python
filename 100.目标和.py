def findTargetSumWays1(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self._findTargetSumWays(nums, 0, S)

    def _findTargetSumWays1(self, nums, index, target):
        if index == len(nums):
            if target == 0:
                return 1
            return 0

        return self._findTargetSumWays(nums, index + 1, target-nums[index])\
                + self._findTargetSumWays(nums, index + 1, target+nums[index])


def findTargetSumWays2(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        mem = dict()
        return self._findTargetSumWays(nums, 0, S, mem)

    def _findTargetSumWays2(self, nums, index, target, mem):
        if index == len(nums):
            if target == 0:
                return 1
            return 0

        tmp = "{},{}".format(index, target)
        if tmp in mem:
            return mem[tmp]

        mem[tmp] = self._findTargetSumWays(nums, index + 1, target-nums[index], mem)\
                    + self._findTargetSumWays(nums, index + 1, target+nums[index], mem)

        return mem[tmp]


def findTargetSumWays3(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum_nums = sum(nums)
        if sum_nums < S or -sum_nums > S:
            return 0
        
        len_nums = len(nums)
        mem = [[0]*(2*sum_nums + 1) for _ in range(len_nums+1)]
        mem[0][sum_nums] = 1
        for i in range(1, len_nums + 1):
            for j in range(2*sum_nums + 1):
                if j + nums[i - 1] < 2*sum_nums + 1:
                    mem[i][j] += mem[i - 1][j + nums[i - 1]]
                if j - nums[i - 1] >= 0:
                    mem[i][j] += mem[i - 1][j - nums[i - 1]]
                    
        return mem[len_nums][sum_nums + S]      

        
print(findTargetSumWays1([1, 1, 1, 1, 1], 3))