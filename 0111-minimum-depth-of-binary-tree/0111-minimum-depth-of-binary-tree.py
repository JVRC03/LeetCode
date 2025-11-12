# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.jvrc = float('inf')
    
    def f(self, root, curr, parent):
        if root is None:
            if parent.left == None and parent.right == None:
                self.jvrc = min(self.jvrc, curr)
            return 
        
        self.f(root.left, curr+1, root)
        self.f(root.right, curr+1, root)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.f(root, 0, root)

        return self.jvrc
        