# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.jvrc = True
    
    def dfs(self, r1, r2):
        if self.jvrc == False:
            return
        if r1 is None and r2 is None:
            return
        
        if r1 is None or r2 is None:
            self.jvrc = False
            return
        
        if r1.val != r2.val:
            self.jvrc = False
            return
        
        self.dfs(r1.left, r2.right)
        self.dfs(r1.right, r2.left)
        
    def isSymmetric(self, root):
        self.dfs(root.left, root.right)

        return self.jvrc
        
       