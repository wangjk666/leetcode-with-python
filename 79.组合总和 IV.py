def combinationSum4(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """    
    if not nums:
        return 0
        
    result = list()
    nums.sort()
    self._combinationSum4(nums, target, list(), result)
    return len(result)

def _combinationSum4(self, nums, target, path, res):
    if target == 0:
        res.append(path)
        return 

    if target < nums[0]:
        return
    
    for i in range(len(nums)):
        self._combinationSum4(nums, target-nums[i], path+[nums[i]], res)

"""
f(i) = sum[ f(i - num) ] for num in nums


class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        mem = [0]*(target + 1)
        mem[0] = 1
        for i in range(1, target +1):
            for num in nums:
                if i >= num:
                    mem[i] += mem[i - num]

        return mem[target]

"""
