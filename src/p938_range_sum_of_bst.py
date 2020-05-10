class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.inorder(root, L, R)
        return self.sum

    def inorder(self, root: TreeNode, L: int, R: int) -> None:
        if not root:
            return
        self.inorder(root.left, L, R)
        if L <= root.val <= R:
            self.sum += root.val
        elif root.val > R:
            return
        self.inorder(root.right, L, R)
