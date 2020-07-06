# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    value = 0

    def isUnivalTree(self, root: TreeNode) -> bool:
        self.value = root.val
        return self.traverse(root)

    def traverse(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.val != self.value:
            return False
        return self.traverse(root.left) and self.traverse(root.right)
