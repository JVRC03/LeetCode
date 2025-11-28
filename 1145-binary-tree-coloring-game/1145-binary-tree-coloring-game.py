# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.parent = None
        self.left_child = None
        self.right_child = None

    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:

        def dfs(root, parent):
            if root is None:
                return 
            
            if root.val == x:
                self.parent = parent
                self.left_child = root.left
                self.right_child = root.right
                return
            
            dfs(root.left, root)
            dfs(root.right, root)
        
        def calc(root):
            if root is None or root.val == x:
                return 0
            
            a = calc(root.left)
            b = calc(root.right)

            return a+b+1

        dfs(root, None)
        b1 = calc(root)
        b2 = calc(self.left_child)
        b3 = calc(self.right_child)
        blue = max(b1, b2, b3)

        red = n-blue

        if blue > red:
            return True 
        
        return False
        