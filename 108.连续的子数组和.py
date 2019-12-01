def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if k == 0:
        return '00' in ''.join(map(str, nums))
    pre_sum = {0:-1}
    cur_sum = 0
    for i, num in enumerate(nums):
        cur_sum = (cur_sum + num)%k
        if cur_sum in pre_sum and i - pre_sum[cur_sum] > 1:
            return True
        if cur_sum not in pre_sum:
            pre_sum[cur_sum] = i
    return False 