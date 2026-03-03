# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None:
            return []
        self.jvrc = []
        dic = {}
        q = deque([root])

        while len(q):
            c = len(q)

            for idx in range(c):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    dic[node.left] = node
                
                if node.right:
                    q.append(node.right)
                    dic[node.right] = node

        vis = set()

        def dfs(root, k, curr):
            if root is None or root in vis:
                return

            vis.add(root)
            if curr == k:
                self.jvrc.append(root.val)
                return 
            
            dfs(root.left, k, curr + 1)
            dfs(root.right, k, curr + 1)
            dfs(dic.get(root), k, curr + 1)

        dfs(target, k, 0)

        return self.jvrc







        