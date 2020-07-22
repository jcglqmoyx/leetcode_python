from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        flag = True
        nodes = [root]
        while nodes:
            values = []
            size = len(nodes)
            for i in range(size):
                node = nodes.pop(0)
                values.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if flag:
                flag = False
            else:
                values.reverse()
                flag = True
            result.append(values)
        return result
