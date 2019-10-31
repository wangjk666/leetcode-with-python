class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelTree(root):
    if root == None:
        return []
    que = []
    num = []
    node = root
    que.append(node)
    num.append(node.val)
    while que:
        node = que.pop(0)
        if node.left == None:
            num.append("null")
        else:
            que.append(node.left)
        if node.right == None:
            num.append("null")
        else:
            que.append(node.right)
            num.append(node.right)
    return num


def isSameTree(p, q):
    pp = levelTree(p)
    qq = levelTree(q)
    if pp == qq:
        return True
    else:
        return False

def isSameTree( p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    else:
        if p.val == q.val:
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        else:
            return False