class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = len_b = 0
        a, b = headA, headB
        while headA:
            len_a += 1
            headA = headA.next
        while headB:
            len_b += 1
            headB = headB.next
        i = 0
        if len_a < len_b:
            while i < len_b - len_a:
                b = b.next
                i += 1
        else:
            while i < len_a - len_b:
                a = a.next
                i += 1
        while a != b:
            a = a.next
            b = b.next
        return a
