class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = ListNode(0)
        result = node
        while head:
            if head.val != val:
                node.next = ListNode(head.val)
                node = node.next
            head=head.next
        return result.next
