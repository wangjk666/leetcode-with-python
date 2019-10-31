class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def height(root):
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1


def postorder(root):
    if root is None:
        return True
    if postorder(root.left) and postorder(root.right):
        return abs(height(root.left) - height(root.right)) <= 1
    else:
        return False

def isBalanced(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return postorder(root)