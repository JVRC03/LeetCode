# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        self.real = None
        self.temp = self.real

        def dfs(root):
            if root is None:
                return 
            
            dfs(root.left)

            if self.temp is not None:
                self.temp.right = TreeNode(root.val)
                self.temp = self.temp.right
            else:
                self.real = TreeNode(root.val)
                self.temp = self.real

            dfs(root.right)

        dfs(root)
        return self.real

        