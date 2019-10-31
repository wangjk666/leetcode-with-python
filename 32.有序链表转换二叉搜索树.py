class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def buildtree(nums, low, high):
    if low > high:
        return None
    if low == high:
        return TreeNode(low)
    mid = (low + high) // 2
    root = TreeNode(nums[mid])
    root.left = buildtree(nums, low, mid-1)
    root.right = buildtree(nums, mid+1, high)
    return root


def sortedListToBST(head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        p = head
        l = []
        while p is not None:
            l.append(p.val)
            p = p.next
        return buildtree(l, 0, len(l)-1)


"""
def sortedListToBST(self, head):
    current, length = head, 0
    while current is not None:
        current, length = current.next, length + 1
    self.head = head
    return self.sortedListToBSTRecu(0, length)

def sortedListToBSTRecu(self, start, end):
    if start == end:
        return None
    mid = start + (end - start) / 2
    left = self.sortedListToBSTRecu(start, mid)
    current = TreeNode(self.head.val)
    current.left = left
    self.head = self.head.next
    current.right = self.sortedListToBSTRecu(mid + 1, end)
    return current
"""