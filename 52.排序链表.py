# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):#合并两个有序的链表
        if not l1:
            return l2
        if not l2:
            return l1
        prenode = ListNode(1)
        p = prenode
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return prenode.next
    
    def sortList(self, head):
        if not head or not head.next:
            return head
        prenode = head
        p1 = prenode
        p2 = prenode
        l = 0
        while p1:
            l += 1
            p1 = p1.next
        mid = l/2
        k = 0
        l1 = prenode
        while p2: # 将单链表从中间一分为二
            if k >= mid-1:
                tmp = p2.next
                p2.next = None
                l2 = tmp
                break
            else:
                p2 = p2.next
                k += 1
        t1 = self.sortList(l1)
        t2 = self.sortList(l2)
        return self.mergeTwoLists(t1,t2)

        