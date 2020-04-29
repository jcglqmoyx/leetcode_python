# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         result = 0
#         while head:
#             result <<= 1
#             result += head.val
#             head = head.next
#         return result


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        dec = [(2 ** idx) * num for idx, num in enumerate(nums[::-1])]
        return sum(dec)
