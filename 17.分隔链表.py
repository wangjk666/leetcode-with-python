class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


def partition(head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = []
        right = []
        target = []
        p = head
        while p:
            if p.val < x:
                left.append(p)
            elif p.val ==x:
                target.append(p)
            else:
                right.append(p)
            p = p.next
        dummy = ListNode(0)
        dummy.next = left[0]
        for i in range(len(left)-1):
            left[i].next = left[i+1]
        left[len(left)-1].next = None
        if len(target) == 0:
            left[len(left)-1].next = right[0]
        else:
            left[len(left)-1].next = target[0]
        for j in range(len(target)-1):
            target[j].next = target[j+1]
        target[len(target)-1].next = right[0]
        for k in range(len(right)-1):
            right[k].next = right[k+1]
        return dummy.next

""""
dummySmaller, dummyGreater = ListNode(-1), ListNode(-1)
smaller, greater = dummySmaller, dummyGreater

while head:
    if head.val < x:
        smaller.next = head
        smaller = smaller.next
    else:
        greater.next = head
        greater = greater.next
    head = head.next

smaller.next = dummyGreater.next
greater.next = None

return dummySmaller.next
"""