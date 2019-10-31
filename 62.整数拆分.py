def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        result = -1
        for i in range(1, n):
            result = max(result, i*(n - i), i * self.integerBreak(n - i))

        return result
