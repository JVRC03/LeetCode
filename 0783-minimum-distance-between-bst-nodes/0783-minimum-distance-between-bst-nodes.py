# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.jvrc = float('inf')
        self.a = float('-inf')
        self.b = float('-inf')

    def dfs(self, root):
        if root is None:
            return
        
        self.dfs(root.left)
        if self.a == float('-inf'):
            self.a = root.val
        else:
            if self.b == float('-inf'):
                self.b = root.val
            else:
                self.a = self.b
                self.b = root.val
        
            self.jvrc = min(self.jvrc, self.b-self.a)

        self.dfs(root.right)

    def minDiffInBST(self, root: Optional[TreeNode]):
        self.dfs(root)
        return self.jvrc
        