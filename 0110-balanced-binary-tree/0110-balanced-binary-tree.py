# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.jvrc = True
    
    def dfs(self, root):
        if root is None or self.jvrc == False:
            return 0
        
        a = self.dfs(root.left)
        b = self.dfs(root.right)

        if abs(a-b) > 1:
            self.jvrc = False
            return 0
        
        return 1+max(a, b)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)

        return self.jvrc
        