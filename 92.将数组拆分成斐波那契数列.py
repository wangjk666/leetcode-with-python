def splitIntoFibonacci(S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        for i in range(1,min(len(S),13)):
            for j in range(i+1,min(len(S),i+13)):
                res.append(int(S[:i]))
                res.append(int(S[i:j]))
                if dfs(S,str(res[0]+res[1]),int(S[:i]), int(S[i:j]),res):
                    return res
                else:
                    res = []
        return res
                

def dfs(s, sum, first, second, res):
    tmp = str(first) + str(second) +sum
    if s == tmp:
        res.append(first+second)
        return True
    if len(s) < len(tmp):
        return False
    if s[:len(tmp)] == tmp:
        res.append(first + second)
        f = str(first)
        return dfs(s[len(f):],str(second+int(sum)), second, first+second, res)
    return False


print(splitIntoFibonacci("123456579"))

