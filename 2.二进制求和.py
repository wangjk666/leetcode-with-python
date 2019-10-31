def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    sum1 = 0
    for i in range(len(a)):
        x = int(a[i])
        sum1 += x*(2**(len(a)-i-1))
    print(sum1)
    sum2 = 0
    for i in range(len(b)):
        y = int(b[i])
        sum2 += y*(2**(len(b)-i-1))
    print(sum2)
    sum3 = sum1 + sum2
    print(sum3)
    res = []
    while sum3 != 0:
        res.append(sum3 % 2)
        sum3 //= 2
    res2 = reversed(res)
    fin = "".join([str(x) for x in res2])
    return fin

str = addBinary("11","1")
print(str)