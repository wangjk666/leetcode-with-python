class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def maxDepth(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return 1 + max(maxDepth(root.left), maxDepth(root.right))