# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def amountOfTime(self, root: Optional[TreeNode], k: int):
        q = deque([root])
        self.tar = None
        dic = {}

        def gt(root, k):
            if root is None or self.tar is not None:
                return 
            
            if root.val == k:
                self.tar = root
                return 
            
            gt(root.left, k)
            gt(root.right, k)

        while len(q):
            c = len(q)

            for i in range(c):
                n = q.popleft()

                if n.right:
                    dic[n.right] = n
                    q.append(n.right)
                
                if n.left:
                    dic[n.left] = n
                    q.append(n.left)
        
        vis = set()

        def dfs(root, curr, dic):
            if root is None or root in vis:
                return 0
            
            vis.add(root)

            a = dfs(root.left, curr + 1, dic)
            b = dfs(root.right, curr + 1, dic)
            c = dfs(dic.get(root), curr + 1, dic)

            return 1 + max(a, b, c)

        gt(root, k)
        return dfs(self.tar, 0, dic)-1
         

      