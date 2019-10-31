class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def buildTree(preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder is None or inorder is None or len(preorder) != len(inorder):
            return None
        index = 0
        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                index = i
        left_pre, right_pre, left_in, right_in = [], [], [], []
        for i in range(index):
            left_pre.append(preorder[i+1])
            left_in.append(inorder[i])
        for j in range(index+1,len(preorder)):
            right_pre.append(preorder[j])
            right_in.append(inorder[j])
        root.left = buildTree(left_pre, left_in)
        root.right = buildTree(right_pre, right_in)
        return root


