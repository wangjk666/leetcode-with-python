def bfs(nums, i, mem, s):
    if i >= len(nums):
        s.add(mem)
        return
    mem.append(nums[i])
    bfs(nums, i + 1, mem, s)
    mem.remove(nums[i])
    bfs(nums, i + 1, mem, s)


def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    s = set()
    mem = []
    bfs(nums, 0, mem, s)
    l = list(s)
    return l


nums = [1, 2, 2]
print(subsetsWithDup(nums))

"""
def subsetsWithDup(self, nums):
    result = []
    self.subsetsWithDupRecu(result, [], sorted(nums))
    return result


def subsetsWithDupRecu(self, result, cur, nums):
    if not nums:
        if cur not in result:
            result.append(cur)
    else:
        self.subsetsWithDupRecu(result, cur, nums[1:])
        self.subsetsWithDupRecu(result, cur + [nums[0]], nums[1:])　　
"""