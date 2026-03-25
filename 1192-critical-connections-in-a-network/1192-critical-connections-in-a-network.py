class Solution:
    def criticalConnections(self, n: int, arr: List[List[int]]) -> List[List[int]]:
        toi, low = [0] * n, [0] * n
        vis = [0] * n
        self.jvrc, dic = [], {}
        self.count = 1

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

        def dfs(source, parent):
            
            if vis[source]:
                return 
            
            vis[source] = 1
            toi[source] = self.count
            low[source] = self.count
            self.count += 1

            a = dic[source]

            for i in range(len(a)):
                
                if a[i] == parent:
                    continue

                if vis[a[i]] == 0:
                    dfs(a[i], source)

                    low[source] = min(low[source], low[a[i]])

                    if low[a[i]] > toi[source]:
                        self.jvrc.append([source, a[i]])
                else:
                    low[source] = min(low[source], toi[a[i]])

        for i in range(len(vis)):
            if not vis[i]:
                dfs(i, -1)

        return self.jvrc



        