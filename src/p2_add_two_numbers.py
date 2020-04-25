class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        head = res
        sum, carry = 0, 0
        while l1 or l2:
            if l1 and l2:
                x = l1.val % 10
                y = l2.val % 10
                sum = x + y + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                x = l1.val % 10
                sum = x + carry
                l1 = l1.next
            else:
                y = l2.val % 10
                sum = y + carry
                l2 = l2.next
            carry = sum // 10
            head.next = ListNode(sum % 10)
            head = head.next
        if carry:
            head.next = ListNode(1)
        return res.next
