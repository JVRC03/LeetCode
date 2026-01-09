# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.s = set()
        self.jvrc = False
    
    def dfs(self, root, k):
        if root is None or self.jvrc:
            return False

        diff = k-root.val

        if diff in self.s:
            self.jvrc = True
            return 
        
        self.s.add(root.val)
        self.dfs(root.left, k)
        self.dfs(root.right, k)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.dfs(root, k)
        return self.jvrc
        