# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.jvrc = 0

        def dfs(root):
            if root is None:
                return [True, 0, float('inf'), float('-inf')]
            
            l = dfs(root.left)
            r = dfs(root.right)

            if l[0] and r[0] and (l[-1] < root.val < r[2]):
                tot = root.val + l[1] + r[1]
                self.jvrc = max(self.jvrc, tot)

                return [True, tot, min(root.val, l[2]), max(root.val, r[3])]

            return [False, 0, float('inf'), float('-inf')]

        dfs(root)
        return self.jvrc
        