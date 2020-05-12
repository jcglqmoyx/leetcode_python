class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        vals1, vals2, sums = [], [], []
        while l1:
            vals1.append(l1.val)
            l1 = l1.next
        while l2:
            vals2.append(l2.val)
            l2 = l2.next
        i, j = len(vals1) - 1, len(vals2) - 1
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                sum = vals1[i] + vals2[j] + carry
                i -= 1
                j -= 1
            elif i >= 0:
                sum = vals1[i] + carry
                i -= 1
            else:
                sum = vals2[j] + carry
                j -= 1
            sums.append(sum % 10)
            carry = sum // 10
        if carry:
            sums.append(1)
        head = result = ListNode(0)
        for index in range(len(sums) - 1, -1, -1):
            head.next = ListNode(sums[index])
            head = head.next
        return result.next
