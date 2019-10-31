class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def level(root, cur, sum):
    if root is None:
        return False
    elif root.left == None and root.right == None:
        return (cur + root.val == sum)
    cur = cur + root.val
    if level(root.left, cur, sum):
        return True
    else:
        return level(root.right, cur, sum)




def hasPathSum(root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return level(root, 0, sum)