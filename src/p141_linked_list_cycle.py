class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         fast = slow = head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#             if fast == slow:
#                 return True
#         return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head != None:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
