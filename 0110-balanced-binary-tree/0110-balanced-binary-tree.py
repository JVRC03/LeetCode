# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.jvrc = True

        def dfs(root):
            if root is None or self.jvrc == False:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            if not self.jvrc:
                return 

            if abs(l - r) > 1:
                self.jvrc = False
                return 
            
            return max(l, r) + 1

        dfs(root)

        return self.jvrc
        