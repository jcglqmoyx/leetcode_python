class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    sum = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.sum

    def traverse(self, root: TreeNode) -> None:
        if not root:
            return
        if root.left and not root.left.left and not root.left.right:
            self.sum += root.left.val
        self.traverse(root.left)
        self.traverse(root.right)
