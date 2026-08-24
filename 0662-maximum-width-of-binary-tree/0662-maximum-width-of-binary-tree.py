# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([[root, 0]])
        jvrc = 1
        
        while len(q):
            c = len(q)
            temp = []
            
            for i in range(c):
                pair = q.popleft()
                node, lv = pair[0], pair[1]
                
                if node.left is not None:
                    q.append([node.left, 2 * lv + 1])
                    temp.append(2 * lv + 1)

                if node.right is not None:
                    q.append([node.right, 2 * lv + 2])
                    temp.append(2 * lv + 2)
            
            if len(temp):
                jvrc = max(jvrc, temp[-1] - temp[0] + 1)
            
        
        return jvrc
            
