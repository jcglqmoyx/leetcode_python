class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        res = ListNode(0)
        head = res
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    head.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    head.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1:
                head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next
            head = head.next
        return res.next
