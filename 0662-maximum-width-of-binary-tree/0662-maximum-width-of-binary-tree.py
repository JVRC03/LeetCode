# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        jvrc = 0
        q = deque([[root, 0]])
        
        while len(q):
            c = len(q)
            a, b = -1, -1
            
            for i in range(c):
                arr = q.popleft()
                n = arr[0]
                val = arr[-1]
                
                if a == -1:
                    a = val
                    b = val
                else:
                    b = val
                
                if n.left:
                    q.append([n.left, (2 * val) + 1])
                if n.right:
                    q.append([n.right, (2 * val) + 2])
            
            jvrc = max(jvrc, (b - a) + 1)
        
        return jvrc
            
