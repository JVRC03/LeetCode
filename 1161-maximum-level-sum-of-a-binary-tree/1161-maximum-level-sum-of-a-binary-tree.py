# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        jvrc, curr = 0, float('-inf')
        c = 1

        while len(q):
            l = len(q)
            s = 0

            for i in range(l):
                n = q.popleft()
                s += n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            
            if s > curr:
                curr = s
                jvrc = c
            
            c += 1
        
        return jvrc

        