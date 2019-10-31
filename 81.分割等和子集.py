def dfs(i,nums,target):
    if i >= len(nums):
        return
    if target == 0:
        return True
    if dfs(i+1,nums,target-nums[i]) == True:
        return True
    else:
        return dfs(i+1,nums,target)


def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    if sum%2 != 0:
        return False
    if dfs(0,nums,sum//2):
        return True
    else:
        return False
def can2(nums):
    l = [0,0]
    for i in range(len(nums)):
        l[0],l[1] = l[1],l[0]+nums[i]
    return 



print(canPartition([1,2,3,5]))
print(canPartition([1,5,11,5]))
