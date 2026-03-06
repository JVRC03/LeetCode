class Solution:
    def validPath(self, n: int, arr: List[List[int]], source: int, k: int) -> bool:
        dic = {}
        self.jvrc = False

        for i in range(len(arr)):
            a, b = arr[i][0], arr[i][1]

            if a not in dic:
                dic[a] = [b]
            else:
                dic[a].append(b)
            
            if b not in dic:
                dic[b] = [a]
            else:
                dic[b].append(a)
        
        vis = [0] * n

        def dfs(source, k):
            if vis[source] or self.jvrc:
                return 
            
            vis[source] = 1
            if source == k:
                self.jvrc = True
                return
            
            a = dic[source]

            for i in range(len(a)):
                dfs(a[i], k)

        dfs(source, k)

        return self.jvrc
        