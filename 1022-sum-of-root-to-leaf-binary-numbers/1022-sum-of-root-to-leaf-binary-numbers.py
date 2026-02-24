# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.jvrc = 0

        def dfs(root, s):
            if root is None:
                return 
            
            if root.left is None and root.right is None:
                self.jvrc += (int(s + str(root.val), 2))
                return
            
            dfs(root.left, s + str(root.val))
            dfs(root.right, s + str(root.val))

        dfs(root, '')

        return self.jvrc
        
        