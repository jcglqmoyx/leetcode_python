class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    index = value = key = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.key = k
        self.inorder(root)
        return self.value

    def inorder(self, root: TreeNode) -> None:
        if not root:
            return
        self.inorder(root.left)
        self.index += 1
        if self.index == self.key:
            self.value = root.val
            return
        self.inorder(root.right)
