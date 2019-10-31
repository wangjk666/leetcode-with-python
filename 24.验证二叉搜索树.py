class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True

    return self.helper(root, float('-inf'), float('inf'))


def helper(self, root, mi, mx):
    if not root:
        return True

    if root.val >= mx or root.val <= mi:
        return False

    return self.helper(root.left, mi, root.val) and self.helper(root.right, root.val, mx)
