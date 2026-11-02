# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
               
        queue = deque([])
        height = 0
        queue.append(root)
        while len(queue) != 0:
            levelsize = len(queue)
            height += 1
            for _ in range(levelsize):
                e = queue.popleft()
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)

        return height