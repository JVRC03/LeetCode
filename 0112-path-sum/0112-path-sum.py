# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def f(self, root, parent, curr, k):
        if root == None:
            if curr == k and parent.left == None and parent.right == None:
                return True
            return False
        
        a = self.f(root.left, root, curr+root.val, k)
        b = self.f(root.right, root, curr+root.val, k)

        return a or b

    def hasPathSum(self, root: Optional[TreeNode], k: int) -> bool:
        if root == None:
            return False

        return self.f(root, root, 0, k)
        