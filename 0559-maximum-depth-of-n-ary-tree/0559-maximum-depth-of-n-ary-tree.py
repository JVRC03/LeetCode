"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.jvrc = 0
    
    def dfs(self, root, curr):
        if root is None:
            return 
        
        self.jvrc = max(self.jvrc, curr)
    
        for i in root.children:
            self.dfs(i, curr+1)
        
    def maxDepth(self, root: 'Node') -> int:
        self.dfs(root, 1)

        return self.jvrc
        