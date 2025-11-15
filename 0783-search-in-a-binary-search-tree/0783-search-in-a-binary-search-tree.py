# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.jvrc = None
    
    def dfs(self, root, k):
        if (root is None) or (self.jvrc is not None):
            return 
        
        if root.val == k:
            self.jvrc = root
            return
        
        self.dfs(root.left, k)
        self.dfs(root.right, k)
        
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.dfs(root, val)

        return self.jvrc
        