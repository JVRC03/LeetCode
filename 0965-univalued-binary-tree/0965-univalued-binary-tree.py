# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.s = set()

        def dfs(root):
            if root is None:
                return True
            
            self.s.add(root.val)
            if len(self.s) > 1:
                return False
            
            return dfs(root.left) and dfs(root.right)

        return dfs(root)
