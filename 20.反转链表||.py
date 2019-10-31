class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

def reverse(head):
    prev = None
    while head is not None:
       next = head.next
       head.next = prev
       prev = head
       head = next
    return prev

def findkth(head, k):
        for i in range(k):
            if head is None:
                return None
            head = head.next
        return head

def reverseBetween(head, m, n):
        dummy = ListNode(-1)
        dummy.next = head
        mth_prev = findkth(dummy, m - 1)
        mth = mth_prev.next
        nth = findkth(dummy, n)
        nth_next = nth.next
        nth.next = None
        reverse(mth)
        mth_prev.next = nth
        mth.next = nth_next
        return dummy.next

