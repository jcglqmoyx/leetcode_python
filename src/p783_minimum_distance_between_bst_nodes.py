import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    min_diff = sys.maxsize
    prev = 0

    def minDiffInBST(self, root: TreeNode) -> int:
        self.prev = root.val
        self.dfs(root)
        return self.min_diff

    def dfs(self, root: TreeNode) -> None:
        if not root:
            return
        self.dfs(root.left)
        diff = root.val - self.prev
        self.prev = root.val
        if self.min_diff > diff > 0:
            self.min_diff = diff
        self.dfs(root.right)
