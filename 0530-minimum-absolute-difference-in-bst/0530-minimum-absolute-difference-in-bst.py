# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.jvrc = float('inf')
        self.curr = -1
    
    def dfs(self, root):
        if root is None:
            return 
        
        self.dfs(root.left)
        if self.curr == -1:
            self.curr = root.val
        else:
            self.jvrc = min(self.jvrc, abs(root.val-self.curr))
            self.curr = root.val
        self.dfs(root.right)
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)

        return self.jvrc
        