def isdivisor(substr, str1):
    if substr == str1:
        return True
    elif substr != str1[:len(substr)]:
        return False
    else:
        return isdivisor(substr, str1[len(substr):])


def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    l1 = len(str1)
    l2 = len(str2)
    l = min(l1, l2)
    sub  = ''
    for i in range(1,l+1):
        substr = str1[:i]
        #print(substr)
        if isdivisor(substr, str1) and isdivisor(substr, str2):
            if len(substr) > len(sub):
                sub = substr
    return sub

        





print(gcdOfStrings('abcabc', 'abc'))