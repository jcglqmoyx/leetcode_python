from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# class Solution:
#     result = []
#
#     def postorder(self, root: 'Node') -> List[int]:
#         self.traverse(root)
#         return self.result
#
#     def traverse(self, node: 'Node') -> None:
#         if not node:
#             return
#         if node.children:
#             for i in range(len(node.children)):
#                 self.traverse(node.children[i])
#         self.result.append(node.val)

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        if not root.children: return [root.val]
        l = []
        for c in root.children: l += self.postorder(c)
        return l + [root.val]
