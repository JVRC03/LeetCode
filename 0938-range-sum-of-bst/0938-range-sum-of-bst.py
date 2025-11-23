# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.jvrc = 0
    
    def dfs(self, root, l, h):
        if root is None:
            return 
        
        if l <= root.val <= h:
            self.jvrc += root.val

        self.dfs(root.left, l, h)
        self.dfs(root.right, l, h) 

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.dfs(root, low, high)

        return self.jvrc
        