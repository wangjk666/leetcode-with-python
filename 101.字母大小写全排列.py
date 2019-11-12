def letterCasePermutation(S):
        res = []
        if not S:
            return [""]
        def dfs(start, tmp):
            if len(tmp) == len(S):  
                res.append(tmp)
                return
            
            c = S[start]
            if c.isdigit():  
                dfs(start + 1, tmp + c)
            elif S[start].islower():
                dfs(start + 1, tmp + c)
                dfs(start + 1, tmp + c.upper())
            else:
                dfs(start + 1, tmp + c)
                dfs(start + 1, tmp + c.lower())

        dfs(0, "")
        return res

print(letterCasePermutation("12345"))