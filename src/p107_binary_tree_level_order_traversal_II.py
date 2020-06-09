from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        nodes = [root]
        while nodes:
            level_values = []
            for i in range(len(nodes), 0, -1):
                node = nodes.pop(0)
                level_values.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(level_values)
        return reversed(result)
