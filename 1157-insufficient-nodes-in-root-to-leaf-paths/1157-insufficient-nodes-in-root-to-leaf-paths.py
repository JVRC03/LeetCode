# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def f(self, root, k, curr):
        if root == None:
            return -1, root
        
        l, a = self.f(root.left, k, curr+root.val)
        r, b = self.f(root.right, k, curr+root.val)

        if l == -1 and r == -1 and curr+root.val < k:
            return 1, None
        
        if l == 1 and r == 1 and ( a!=None or b!=None):
            root.left = a
            root.right = b
            return 1, root

        if l == 1:
            if a == None:
                return 1, None
            root.left = a

        if r == 1:
            if b == None:
                return 1, None
            root.right = b

        return 1, root

           

    def sufficientSubset(self, root: Optional[TreeNode], k: int) -> Optional[TreeNode]:
        jv, rc = self.f(root, k, 0)
        return rc
        