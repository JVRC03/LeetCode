# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def f(self, root):
        if root == None:
            return True
        
        a = self.f(root.left)
        b = self.f(root.right)

        if root.val == 0:
            return False
        if root.val == 1:
            return True

        if root.val == 2:
            if (a or b):
                return True
            return False
        
        if a and b:
            return True
        
        return False
        
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        return self.f(root)
        