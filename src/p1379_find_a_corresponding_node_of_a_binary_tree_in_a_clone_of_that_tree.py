class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     result = None
#
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         self.traverse(cloned, target)
#         return self.result
#
#     def traverse(self, cloned: TreeNode, target: TreeNode) -> None:
#         if not cloned:
#             return
#         if cloned.val == target.val:
#             self.result = cloned
#             return
#         self.traverse(cloned.left, target)
#         self.traverse(cloned.right, target)

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or original == target:
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left
        else:
            return self.getTargetCopy(original.right, cloned.right, target)
