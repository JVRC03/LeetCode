class Solution:
    def accountsMerge(self, arr: List[List[str]]):
        jvrc, a = [], []
        dic, main = {}, {}
        parent = [i for i in range(len(arr))]
        rank = [0] * len(arr)

        def findParent(node):
            if node == parent[node]:
                return node
            
            parent[node] = findParent(parent[node])
            return parent[node]

        def union(u, v):
            ult_u = findParent(u)
            ult_v = findParent(v)

            if ult_u == ult_v:
                return
            
            if rank[ult_u] < rank[ult_v]:
                parent[ult_u] = ult_v
            elif rank[ult_v] < rank[ult_u]:
                parent[ult_v] = ult_u
            else:
                parent[ult_v] = ult_u
                rank[ult_u] += 1

        for i in range(len(arr)):
            main[i] = []
            for j in range(1, len(arr[i])):
                if arr[i][j] not in dic:
                    dic[arr[i][j]] = i
                    a.append([arr[i][j], i])
                else:
                    union(i, dic[arr[i][j]])

        for i in range(len(a)):
            val = findParent(a[i][1])
            main[val].append(a[i][0])
        
        for i in main:
            k = [arr[i][0]]
            temp = main[i]
            temp.sort()
            k.extend(temp)

            if len(k) > 1:
                jvrc.append(k)

        return jvrc
        