# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        self.jvrc = []

        if root is None:
            return []

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
            
            self.jvrc.append(temp)
        
        return self.jvrc

        