class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(nums, l, r):
    if l > r:
        return None
    if l == r:
        return TreeNode(nums[l])
    mid = (l + r) // 2
    root = TreeNode(nums[mid])
    root.left = buildTree(nums, l, mid-1)
    root.right = buildTree(nums, mid+1, r)
    return root

def sortedArrayToBST(nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return buildTree(nums, 0, len(nums)-1)

