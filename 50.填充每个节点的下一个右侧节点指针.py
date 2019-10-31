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
        if root==None:
            return None
        start = root
        cur = None
        while start.left:
            cur = start
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            start = start.left
        return root


        