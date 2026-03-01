class Solution:
    def specialNodes(self, n: int, arr: List[List[int]], x: int, y: int, z: int) -> int:
        dic, parent = {}, {}

        for i in range(len(arr)):
            a, b = arr[i][0], arr[i][1]
            if a > b:
                a, b = b, a
            
            if a not in dic:
                dic[a] = [b]
            else:
                dic[a].append(b)
                    
        for i in dic:
            temp = dic[i]

            for j in range(len(temp)):
                parent[temp[j]] = i

        def bfs(k, n):
            temp = {}
            for i in range(n):
                temp[i] = 0

            vis = set()

            q = deque([k])
            curr = 0

            while len(q):
                c = len(q)
                curr += 1

                for i in range(c):
                    node = q.popleft()
                    vis.add(node)

                    if node in dic:
                        a = dic[node]

                        for j in range(len(a)):
                            if a[j] not in vis:
                                vis.add(a[j])
                                q.append(a[j])
                                temp[a[j]] = curr                        
                    
                    if node in parent:
                        a = [parent[node]]

                        for j in range(len(a)):
                            if a[j] not in vis:
                                vis.add(a[j])
                                q.append(a[j])
                                temp[a[j]] = curr
                    
            return temp

        dic1 = bfs(x, n)
        dic2 = bfs(y, n)
        dic3 = bfs(z, n)
        
        jvrc = 0

        for i in range(n):
            ar = [dic1[i], dic2[i], dic3[i]]
            ar.sort()

            a, b, c = ar[0], ar[1], ar[2]

            if a**2 + b**2 == c**2:
                jvrc += 1

        return jvrc
        