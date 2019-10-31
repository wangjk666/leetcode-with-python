class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def left_inorder(root, l):
    if root is None:
        return
    left_inorder(root.left, l)
    l.append(root)
    left_inorder(root.right, l)


def right_inorder(root, l):
    if root is None:
        return
    right_inorder(root.right, l)
    l.append(root)
    right_inorder(root.left, l)


def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    l = []
    r = []
    left_inorder(root, l)
    right_inorder(root, r)
    if l == r:
        return True
    else:
        return False


""""
def isSymmetric(self, root):
    if root is None:
        return True

    return self.isSymmetricRecu(root.left, root.right)

def isSymmetricRecu(self, left, right):
    if left is None and right is None:
        return True
    if left is None or right is None or left.val != right.val:
        return False
    return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)
"""