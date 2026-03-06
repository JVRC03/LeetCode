class Solution:
    def canFinish(self, n: int, arr: List[List[int]]) -> bool:
        vis = [0] * n
        dic = {}

        for i in range(len(arr)):
            a, b = arr[i][0], arr[i][1]

            if a not in dic:
                dic[a] = [b]
            else:
                dic[a].append(b)
            
            vis[b] += 1
        
        q = deque([])

        for i in range(len(vis)):
            if not vis[i]:
                q.append(i)
        
        jvrc = 0

        while len(q):
            c = len(q)

            for idx in range(c):
                node = q.popleft()
                jvrc += 1
                if node not in dic:
                    continue
                
                a = dic[node]

                for i in range(len(a)):
                    vis[a[i]] -= 1

                    if not vis[a[i]]:
                        q.append(a[i])  
        
        if jvrc != n:
            return False
        
        return True