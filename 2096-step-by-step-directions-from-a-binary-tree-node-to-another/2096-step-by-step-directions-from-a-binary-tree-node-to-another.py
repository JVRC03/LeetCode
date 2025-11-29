# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.l = []
        self.r = []
    
    def dfs(self, root, a, b, arr):
        if root is None:
            return 
        
        if root.val == a:
            self.l = arr.copy()
        if root.val == b:
            self.r = arr.copy()

        arr.append('L')
        self.dfs(root.left, a, b, arr)
        arr.pop()

        arr.append('R')
        self.dfs(root.right, a, b, arr)
        arr.pop()


    def getDirections(self, root: Optional[TreeNode], a: int, b: int) -> str:
        self.dfs(root, a, b, [])
        jvrc = ''

        self.l = self.l[::-1]
        self.r = self.r[::-1]

        while len(self.l) and len(self.r):
            if self.l[-1] == self.r[-1]:
                self.l.pop()
                self.r.pop()
                continue
            break
        
        self.r = self.r[::-1]
        jvrc += ('U' * len(self.l))
        jvrc += (''.join(self.r))

        return jvrc


                
            
        