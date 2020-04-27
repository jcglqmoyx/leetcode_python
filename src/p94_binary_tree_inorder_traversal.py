from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        self.traversal(root, ret)
        return ret

    def traversal(self, root: TreeNode, ret: List[int]) -> None:
        if not root: return
        self.traversal(root.left, ret)
        ret.append(root.val)
        self.traversal(root.right, ret)
