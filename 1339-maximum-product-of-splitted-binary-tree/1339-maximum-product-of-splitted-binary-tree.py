# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tot = 0
        self.jvrc = 0

    def maxProduct(self, root: Optional[TreeNode]):

        def dfs(root):
            if root is None:
                return 
            
            self.tot += root.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        def f(root):
            if root is None:
                return 0
            
            a = f(root.left)
            b = f(root.right)

            l_sum = root.val+a+b
            r_sum = self.tot-l_sum

            self.jvrc = max(self.jvrc, (l_sum * r_sum))

            return l_sum

        f(root)
        return self.jvrc%1000000007
        