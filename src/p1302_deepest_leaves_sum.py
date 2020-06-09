import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def deepestLeavesSum(self, root: TreeNode) -> int:
#         sum = 0
#         nodes = [root]
#         while nodes:
#             sum = 0
#             for i in range(len(nodes), 0, -1):
#                 node = nodes.pop(0)
#                 sum += node.val
#                 if node.left:
#                     nodes.append(node.left)
#                 if node.right:
#                     nodes.append(node.right)
#         return sum


class Solution:
    def deepestLeavesSum(self, root):
        sum = collections.Counter()

        def dfs(node, depth):
            if node:
                sum[depth] += node.val
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root, 0)
        return sum[max(sum)]
