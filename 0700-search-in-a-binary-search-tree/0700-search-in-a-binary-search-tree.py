# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.jvrc = None

        def dfs(root, k):
            if root is None or self.jvrc is not None:
                return 0
            
            if root.val == k:
                self.jvrc = root
                return 0
            
            return dfs(root.left, k) | dfs(root.right, k)

        dfs(root, val)
        return self.jvrc
        