# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        level = xy_level = xy_parent = 0
        nodes = [root]
        while nodes:
            level += 1
            for i in range(len(nodes), 0, -1):
                node = nodes.pop(0)
                parent = node.val
                if node.left:
                    if node.left.val == x or node.left.val == y:
                        if xy_level == level and xy_parent != parent:
                            return True
                        xy_level, xy_parent = level, parent
                    nodes.append(node.left)
                if node.right:
                    if node.right.val == x or node.right.val == y:
                        if xy_level == level and xy_parent != parent:
                            return True
                        xy_level, xy_parent = level, parent
                    nodes.append(node.right)
        return False


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.right = node4
node3.right = node5
print(Solution().isCousins(node1, 5, 4))
