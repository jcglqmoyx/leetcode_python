from typing import List
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        nodes = []
        nodes.append(root)
        while nodes:
            sum = 0
            count = len(nodes)
            for i in range(len(nodes) - 1, -1, -1):
                node = nodes.pop(0)
                sum += node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(sum / count)
        return result
