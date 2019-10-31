def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    red = 0
    white = 0
    blue = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            red += 1
        elif nums[i] == 1:
            white += 1
        else:
            blue += 1
    for j in range(red):
        nums[i] = 0
    for k in range(white):
        nums[red+k] = 1
    for m in range(blue):
        nums[red+white+m] = 2