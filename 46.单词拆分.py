def cutword(self, worddict, s):
    if s in worddict:
        return True
    for i in range(len(s)):
        if s[:i] in worddict:
            return self.cutword(worddict, s[i:])
    return False

def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    return self.cutword(wordDict, s)


"""
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        bp = [0]

        for i in range(len(s)+1):
            for j in bp:
                if s[j:i] in wordDict:
                    bp.append(i)
                    break

        return bp[-1] == len(s)

"""