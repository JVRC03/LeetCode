class Solution:
    def shortestBridge(self, mat: List[List[int]]) -> int:
        q = deque([])
        vis = set()
        c = 0

        def dfs(mat, i, j, c):
            if i >= len(mat) or j >= len(mat[0]) or i < 0 or j < 0 or mat[i][j] == -1 or mat[i][j] == 0:
                return
            
            if c%2 == 0:
                q.append([i, j])
            else:
                vis.add((i, j))

            mat[i][j] = -1

            dfs(mat, i, j+1, c)
            dfs(mat, i, j-1, c)
            dfs(mat, i+1, j, c)
            dfs(mat, i-1, j, c)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    dfs(mat, i, j, c)
                    c += 1
        
        self.jvrc = 0
        print(q)
        while len(q):
            car = len(q)

            for idx in range(car):
                pair = q.popleft()

                i, j = pair[0], pair[1]

                if i < len(mat) and j+1 < len(mat[0]):
                    if mat[i][j+1] == 0:
                        mat[i][j+1] = -1
                        q.append([i, j+1])
                    else:
                        if (i, j+1) in vis:
                            return self.jvrc
                
                if i < len(mat) and j-1 > -1:
                    if mat[i][j-1] == 0:
                        mat[i][j-1] = -1
                        q.append([i, j-1])
                    else:
                        if (i, j-1) in vis:
                            return self.jvrc
                
                if i+1 < len(mat) and j < len(mat[0]):
                    if mat[i+1][j] == 0:
                        mat[i+1][j] = -1
                        q.append([i+1, j])
                    else:
                        if (i+1, j) in vis:
                            return self.jvrc
                
                if i-1 > -1 and j < len(mat[0]):
                    if mat[i-1][j] == 0:
                        mat[i-1][j] = -1
                        q.append([i-1, j])
                    else:
                        if (i-1, j) in vis:
                            return self.jvrc

            self.jvrc += 1
        
        return Fola_Fuski

        