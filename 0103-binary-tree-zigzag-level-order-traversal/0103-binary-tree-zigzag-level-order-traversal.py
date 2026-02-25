# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([root])
        self.jvrc = []
        cnt = 0

        while len(q):
            c = len(q)
            temp = []

            for i in range(c):
                node = q.popleft()
                temp.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if cnt%2 == 0:
                self.jvrc.append(temp)
            else:
                temp = temp[::-1]
                self.jvrc.append(temp)
            
            cnt += 1
        
        return self.jvrc



        