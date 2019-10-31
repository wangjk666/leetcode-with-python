def countArrangement(N):
        """
        :type N: int
        :rtype: int
        """
        nums = []
        for i in range(1,N+1):
            nums.append(i)
        re = []
        permute(nums,[],re)
        return len(re)



def permute(nums,te,re):
    if not nums:
        flag = 1
        for j in range(len(te)):
            if (j+1)%te[j] and te[j]%(j+1):
                flag = 0
        if flag == 1:
            re.append(te)
    else:
        for i in range(len(nums)):
            permute(nums[:i]+nums[i+1:],te+[nums[i]],re)


print(countArrangement(2))
    