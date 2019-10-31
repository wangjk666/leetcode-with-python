def isSubsequence(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) < len(s):
            return False
        last = 0
        for i in range(len(s)):
            tmp = s[i]
            for j in range(last,len(t)):
                if t[j] == tmp:
                    last = j+1
                    break
            if j == len(t)-1 and t[j]!= tmp:
                return False
        return True


s = "axc"
t= "ahbgdc"
print(isSubsequence(s,t))