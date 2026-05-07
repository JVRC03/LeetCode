# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        arr = set()

        def dfs(root):
            if root is None:
                return 
            
            arr.add(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        if len(arr) < 2:
            return -1

        arr = list(arr)
        arr.sort()

        return arr[1]        