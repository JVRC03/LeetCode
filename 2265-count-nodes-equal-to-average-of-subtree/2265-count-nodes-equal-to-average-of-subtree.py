# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.jvrc = 0

        def dfs(root):
            if root is None:
                return [0, 0]

            a = dfs(root.left)
            b = dfs(root.right)

            left, right = a[0], b[0]
            c1, c2 = a[1], b[1]

            if ((root.val + left + right) // (1 + c1 + c2)) == root.val:
                self.jvrc += 1
         
            return [root.val + left + right, 1 + c1 + c2]

        dfs(root)
        return self.jvrc
        