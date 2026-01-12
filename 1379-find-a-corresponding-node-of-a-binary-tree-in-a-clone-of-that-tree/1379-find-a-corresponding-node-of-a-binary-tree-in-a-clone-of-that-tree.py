# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.jvrc = None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode):

        def dfs(root, k):
            if self.jvrc is not None or root is None:
                return 
            
            if root.val == k.val:
                self.jvrc = root
                return 
            
            dfs(root.left, k)
            dfs(root.right, k)

        dfs(cloned, target)
        return self.jvrc

        