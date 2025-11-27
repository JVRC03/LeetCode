# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.jvrc = None
        self.temp = None
    
    def dfs(self, root):
        if root is None:
            return 
        
        self.dfs(root.left)
        node = TreeNode()
        node.val = root.val

        if self.jvrc == None:
            self.jvrc = node
            self.temp = node
        else:
            self.temp.right = node
            self.temp = node
        
        self.dfs(root.right)

    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)

        return self.jvrc

        