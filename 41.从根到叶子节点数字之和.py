class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def sumNumbers(self, root):
    return self.sumNumbersRecu(root, 0)


def sumNumbersRecu(self, root, num):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return num * 10 + root.val

    return self.sumNumbersRecu(root.left, num * 10 + root.val) + self.sumNumbersRecu(root.right, num * 10 + root.val)


"""
    def sumNumbers(self, root):
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, value):
        if root:
            #if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.left, value*10+root.val)
            #if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.right, value*10+root.val)
            if not root.left and not root.right:
                self.res += value*10 + root.val　
                
                
    def sumNumbers1(self, root):
    if not root:
        return 0
    stack, res = [(root, root.val)], 0
    while stack:
        node, value = stack.pop()
        if node:
            if not node.left and not node.right:
                res += value
            if node.right:
                stack.append((node.right, value*10+node.right.val))
            if node.left:
                stack.append((node.left, value*10+node.left.val))
    return res
    
"""