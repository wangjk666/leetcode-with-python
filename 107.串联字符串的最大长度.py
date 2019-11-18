def frequency(words):
    d= {}
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    for key in d.keys():
        if d[key] > 1:
            return False
    return True 
    
    


def dfs(i, arr, tmp, res):
    if i >= len(arr):
        res.append(tmp)
        return
    flag = 1
    if frequency(arr[i]) == False:
        flag = 0
    for j in arr[i]:
        if j in tmp:
            flag = 0
            break
    if flag == 1:
        dfs(i+1, arr, tmp+arr[i], res)
        dfs(i+1, arr, tmp, res)
    else:
        dfs(i+1, arr, tmp, res)


def maxLength(arr):
    """
    :type arr: List[str]
    :rtype: int
    """
    res = []
    dfs(0, arr, "", res)
    res.sort()
    return len(res[len(res)-1])


print(maxLength(["un","iq","ue"]))