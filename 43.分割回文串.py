def partition(self, s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    if len(s) == 0:
        return []
    else:
        res = []
        self.partition_helper(s, [], res)
    return res


def partition_helper(self, s, cur_res, result):
    if len(s) == 0:
        result.append(cur_res)
    for i in range(1, len(s) + 1):
        if self.check(s[:i]):
            self.partition_helper(s[i:], cur_res + [s[:i]], result)


def check(self, s):
    if len(s) == 0:
        return False
    else:
        start = 0
        end = len(s) - 1
        while start <= end:
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True


