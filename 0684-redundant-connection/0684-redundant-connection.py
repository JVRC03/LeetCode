class Solution:
    def findRedundantConnection(self, arr: List[List[int]]) -> List[int]:
        n = -1
        for i in range(len(arr)):
            n = max(n, arr[i][0], arr[i][1])
        
        parent = [i for i in range(n+1)]
        rank = [0] * (n + 1)

        jvrc = [-1, -1]

        def findParent(node):
            if parent[node] == node:
                return node
            
            parent[node] = findParent(parent[node])
            return parent[node]

        def union(u, v):
            ult_u = findParent(u)
            ult_v = findParent(v)

            if parent[ult_u] == parent[ult_v]:
                return True
            
            if rank[ult_u] < rank[ult_v]:
                parent[ult_u] = ult_v
            elif rank[ult_v] < rank[ult_u]:
                parent[ult_v] = ult_u
            else:
                parent[ult_u] = ult_v
                rank[ult_v] += 1
            
            return False

        for i in range(len(arr)):
            if union(arr[i][0], arr[i][1]):
                jvrc[0] = arr[i][0]
                jvrc[1] = arr[i][1]

        return jvrc
        