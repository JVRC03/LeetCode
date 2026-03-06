class Solution:
    def validPath(self, n: int, arr: List[List[int]], source: int, k: int) -> bool:
        dic = {}

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

        def bfs(source, k):
            q = deque([source])

            while len(q):
                c = len(q)

                for idx in range(c):
                    node = q.popleft()

                    if node == k:
                        return True
                    
                    a = dic[node]
                    vis[node] = 1
                    for i in range(len(a)):
                        if vis[a[i]] == 0:
                            vis[a[i]] = 1
                            q.append(a[i])
                            if a[i] == k:
                                return True
                    
            return False


        return bfs(source, k)
        