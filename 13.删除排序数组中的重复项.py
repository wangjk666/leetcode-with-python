def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = {}
    for i in range(len(nums)):
        dic[nums[i]] = nums.count(nums[i])
    for i in range(len(nums)):
        nums.pop()
    for key in dic.keys():
        if dic[key] >= 3:
            dic[key] = 2
    for key in dic.keys():
        for i in range(dic[key]):
            nums.append(key)
    return len(nums)


nums = [0, 0, 0, 1, 1, 2]
print(removeDuplicates(nums))
