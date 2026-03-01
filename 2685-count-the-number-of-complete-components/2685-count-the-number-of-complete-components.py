class Solution:
    def countCompleteComponents(self, n: int, arr: List[List[int]]) -> int:
        jvrc, vis = 0, [0] * n
        dic = {}

        for i in range(n):
            dic[i] = []

        for i in range(len(arr)):
            a, b = arr[i][0], arr[i][1]

            dic[a].append(b)
            dic[b].append(a)

        def bfs(source):
            nodes, edges = 1, 0
            q = deque([source])
            vis[source] = 1
            st = set()

            while len(q):
                c = len(q)

                for i in range(c):
                    node = q.popleft()

                    a = dic[node]

                    for j in range(len(a)):
                        if not vis[a[j]]:
                            vis[a[j]] = 1
                            nodes += 1
                            q.append(a[j])
                        
                        x, y = (node, a[j]), (a[j], node)

                        if x not in st and y not in st:
                            st.add(x)
                            edges += 1

            return nodes, edges
            
        for i in range(len(vis)):
            if not vis[i]:
                nodes, edges = bfs(i)

                nodes -= 1
                nodes = (nodes * (nodes + 1))//2
            
                if nodes == edges:
                    jvrc += 1
            
        return jvrc

        