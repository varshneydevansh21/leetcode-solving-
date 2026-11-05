# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.maxi = float("-inf")

        def Solve(node):
            if not node:
                return 0
            left = max(0, Solve(node.left))
            right = max(0, Solve(node.right))
            self.maxi = max(self.maxi, left + right + node.val)
            return node.val + max(left, right)

        Solve(root)
        return self.maxi
