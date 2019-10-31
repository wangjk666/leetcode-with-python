class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root
        node_next = self.get_next_node(root.next)
        if root.left and root.right:
            root.left.next = root.right
            root.right.next = node_next
        elif root.left:
            root.left.next = node_next
        else:
            root.right.next = node_next
        self.connect(root.right)  # 注意要先连接右边,不然左边找的node_next为空
        self.connect(root.left)
        return root
    
        
    def get_next_node(self,root):
        node = root
        while node:
            if node.left:
                return node.left
            if node.right:
                return node.right
            node = node.next
        return node
                
        