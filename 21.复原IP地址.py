def isvalid(s):
    num = 0
    for i in range(len(s)):
        num = num * 10 + (s[i] - '0')
    if len(s) > 1:
        return s[0] != 0 and 0 <= num < 256
    else:
        return 0 <= num < 256


def dfs(t, s, l, count):
    if count == 3 and isvalid(s):
        l.append(t + s)
        return
    ran = min(len(s), 4)
    for i in range(1, ran):
        sub = s[0:i]
        if isvalid(sub):
            dfs(t+sub+".",s[i:], l, count+1)

def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    result = []
    t = ""
    dfs(t, s, result, 0)
    return result