re = []
def readBinaryWatch(num):
    """
    :type num: int
    :rtype: List[str]
    """
    tmp = [0 for _ in range(10)]
    dfs(0,num,tmp)
    return re


def dfs(i,num,tmp):
    if num == 0:
        print(tmp)
        s = array_to_time(tmp)
        print(s)
        re.append(s)
        return
    elif i >= len(tmp):
        return
    tmp[i] = 1
    dfs(i+1,num-1,tmp)
    tmp[i] = 0
    dfs(i+1,num,tmp)


def array_to_time(s):
    print(s)
    hi = 0
    mi = 0
    for i in range(4):
        hi += s[i]*pow(2,3-i)
    for j in range(4,10):
        mi += s[j]*pow(2,9-j)
    if hi > 11 or mi > 59:
        return
    else:
        h = str(hi)
        m = ""
        if mi <= 9:
            m = "0"+str(mi)
        else:
            m = str(mi)
    return h+":"+m

        

print(readBinaryWatch(1))

    

