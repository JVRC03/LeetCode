class Solution:
    def minScore(self, n: int, g: List[List[int]]) -> int:
        dic = {}
        vis = [0] * (n+1)
        for i in range(len(g)):
            if g[i][0] not in dic:
                dic[g[i][0]] = [[g[i][1], g[i][-1]]]
            else:
                dic[g[i][0]].append([g[i][1], g[i][-1]])

            if g[i][1] not in dic:
                dic[g[i][1]] = [[g[i][0], g[i][-1]]]
            else:
                dic[g[i][1]].append([g[i][0], g[i][-1]])
        
        s = set()
        self.jvrc = float('inf')

        def dfs(node):
            if node not in dic:
                return 
            
            if vis[node] == 1:
                return
            vis[node] = 1

            arr = dic[node]

            for i in range(len(arr)):
                self.jvrc = min(self.jvrc, arr[i][-1])
                dfs(arr[i][0])

        dfs(1)
        return self.jvrc
        
            