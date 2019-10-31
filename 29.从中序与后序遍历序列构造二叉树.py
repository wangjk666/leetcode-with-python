class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def buildTree(inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder is None or postorder is None or len(inorder) != len(postorder):
            return None
        root = TreeNode(postorder[-1])
        n = inorder.index(postorder[-1])
        root.left = buildTree(inorder[:n], postorder[:n])
        root.right = buildTree(inorder[n+1:], postorder[n:-1])
        return root