class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def levelOrderBottom(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result, queue = [], [root]
        while queue:
            vals = []
            for i in range(len(queue)):
                node = queue.pop(0)
                vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if vals:
                result.append(vals)
        result.reverse()
        return result


