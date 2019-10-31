def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    intNum = 0
    for i in range(len(digits)):
        intNum = intNum * 10 + digits[i]
    intNum += 1
    # 数字转换成字符
    strNum = str(intNum)
    # 字符转换成数组
    res = []
    for i in range(len(strNum)):
        res.append(int(strNum[i]))
    return res

