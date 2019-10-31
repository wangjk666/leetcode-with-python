class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generateTreesRecu(low, high):
    result = []
    if low > high:
        result.append(None)
    for i in range(low, high+1):
        left = generateTreesRecu(low, i-1)
        right = generateTreesRecu(i+1, high)
        for j in left:
            for k in right:
                cur = TreeNode(i)
                cur.left = j
                cur.right = k
                result.append(cur)
    return result


def generateTrees(n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return generateTreesRecu(1, n)

