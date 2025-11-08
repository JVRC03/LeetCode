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
            main = []

            for i in range(c):
                arr = q.popleft()
                main.append(arr[-1])

                if arr[0].left:
                    q.append([arr[0].left, (arr[-1]*2)+1])
                if arr[0].right:
                    q.append([arr[0].right, (2*arr[-1])+2])
            
            jvrc = max(jvrc, 1+(main[-1]-main[0]))
        
        return jvrc
        