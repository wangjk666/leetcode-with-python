class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def minDepth(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is not None:
            return 1 + minDepth(root.right)
        elif root.left is not None and root.right is None:
            return 1 + minDepth(root.left)
        elif root.left is None and root.right is None:
            return 1
        left = minDepth(root.left)
        right = minDepth(root.right)
        return 1 + min(left, right)