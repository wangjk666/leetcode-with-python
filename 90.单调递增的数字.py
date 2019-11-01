def monotoneIncreasingDigits(N):
    """
    :type N: int
    :rtype: int
    """
    s=list(str(N))
    maker=len(s)
    for i in range(maker-1,0,-1):
        if s[i]<s[i-1]:
            maker,s[i-1]=i,str(int(s[i-1])-1)
            s[maker:]=['9']*(len(s)-maker)
    return int(''.join(s))


print(monotoneIncreasingDigits(10))   