class Solution:
    def largestIsland(self, mat: List[List[int]]) -> int:
        jvrc = 0
        temp = []
        parent = [i for i in range(len(mat) * len(mat))]
        dic = {}
        self.count = 0

        for i in range(len(mat)):
            g = []
            for j in range(len(mat)):
                g.append(mat[i][j])
            temp.append(g)

        def dfs(i, j, source):
            if i >= len(temp) or j >= len(mat) or i < 0 or j < 0 or temp[i][j] != 1:
                return
            
            self.count += 1
            temp[i][j] = 'JVRC'
            node = (i * len(mat)) + j
            parent[node] = source

            dfs(i+1, j, source)
            dfs(i-1, j, source)
            dfs(i, j+1, source)
            dfs(i, j-1, source)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    source = (i * len(mat)) + j
                    self.count = 0
                    dfs(i, j, source)
                    dic[source] = self.count
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    node = (i * len(mat)) + j
                    s = set()

                    if i-1 >= 0 and mat[i-1][j] == 1:
                        s.add(parent[node - len(mat)])
                    
                    if i+1 < len(mat) and mat[i+1][j] == 1:
                        s.add(parent[node + len(mat)])
                    
                    if j-1 >= 0 and mat[i][j-1] == 1:
                        s.add(parent[node - 1])
                    
                    if j+1 < len(mat) and mat[i][j+1] == 1:
                        s.add(parent[node + 1])

                    local = 0
                    l = list(s)
                    for k in range(len(l)):
                        local += dic[l[k]]
                    
                    jvrc = max(jvrc, local + 1)

        if jvrc == 0:
            return len(mat) * len(mat)
        return jvrc