class Solution:
    def containsCycle(self, mat: List[List[str]]) -> bool:
        glob_vis = set()
        self.cycle = False

        def bfs(mat, i, j, k):
            q = deque([[i, j]])
            vis = set()

            while len(q):
                c = len(q)

                for idx in range(c):
                    pair = q.popleft()

                    i, j = pair[0], pair[1]
                    mat[i][j] = 0

                    glob_vis.add((i, j))

                    if i < len(mat) and j+1 < len(mat[0]) and mat[i][j+1] == k:
                        q.append([i, j+1])
                        if (i, j+1) in vis:
                            self.cycle = True
                            return
                        vis.add((i, j+1))
                    
                    if i < len(mat) and j-1 > -1 and mat[i][j-1] == k:
                        q.append([i, j-1])
                        if (i, j-1) in vis:
                            self.cycle = True
                            return
                        vis.add((i, j-1))
                    
                    if i+1 < len(mat) and mat[i+1][j] == k:
                        q.append([i+1, j])
                        if (i+1, j) in vis:
                            self.cycle = True
                            return
                        vis.add((i+1, j))
                    
                    if i-1 > -1 and mat[i-1][j] == k:
                        q.append([i-1, j])
                        if (i-1, j) in vis:
                            self.cycle = True
                            return
                        vis.add((i-1, j))


            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i, j) not in glob_vis:
                    bfs(mat, i, j, mat[i][j])

                    if self.cycle:
                        return True
        
        return False
        