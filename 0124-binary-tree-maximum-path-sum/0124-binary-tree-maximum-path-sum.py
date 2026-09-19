# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.jvrc = float('-inf')

        def dfs(root):
            if root is None:
                return float('-inf')

            a = dfs(root.left)
            b = dfs(root.right)

            glob = root.val + a + b
            left = root.val + a
            right = root.val + b

            self.jvrc = max(self.jvrc, glob, left, right, root.val)

            return max(left, right, root.val)

        dfs(root)
        return self.jvrc
        