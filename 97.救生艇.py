def numRescueBoats(people, limit):
    """
    :type people: List[int]
    :type limit: int
    :rtype: int
    """
    n=len(people)
        people.sort()
        res=0
        left=0
        right=n-1
        while left<=right:
            if people[left]+people[right]<=limit:
                res+=1
                left+=1
                right-=1
            else:
                res+=1
                right-=1
        return res




print(numRescueBoats([5,1,4,2],6))