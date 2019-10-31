def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    i = 0
    while nums[i] < nums[i+1]:
        i += 1
    for j in range(i+1):
        nums.append(nums[j])
    for j in range(i+1):
        nums.remove(nums[j])
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


list = [2,5,6,0,0,1,2]
print (search(list,2))