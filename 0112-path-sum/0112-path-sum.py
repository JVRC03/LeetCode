# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], k: int) -> bool:
        
        def dfs(root, k, curr):
            if root is None:
                return False
            if root.left is None and root.right is None:
                if curr + root.val == k:
                    return True
                return False

            return dfs(root.left, k, curr + root.val) or dfs(root.right, k, curr + root.val)

        return dfs(root, k, 0)
        