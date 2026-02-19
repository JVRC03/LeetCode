class Solution:
    def orangesRotting(self, mat: List[List[int]]) -> int:
        q = deque([])
        self.jvrc = 0
        rott, not_rott = 0, 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 2:
                    q.append([i, j])
                    rott += 1
                elif mat[i][j] == 1:
                    not_rott += 1
        
        if rott == 0 and not_rott == 0:
            return 0
        
        if rott == 0:
            return -1
        
        if not_rott == 0:
            return 0
        
        while len(q):
            c = len(q)

            for i in range(c):
                n = q.popleft()

                a, b = n[0], n[1]

                if a < len(mat) and b+1 < len(mat[0]) and mat[a][b+1] == 1:
                    q.append([a, b+1])
                    mat[a][b+1] = 2

                if a < len(mat) and b-1 > -1 and mat[a][b-1] == 1:
                    q.append([a, b-1])
                    mat[a][b-1] = 2
                
                if a+1 < len(mat) and b < len(mat[0]) and mat[a+1][b] == 1:
                    q.append([a+1, b])
                    mat[a+1][b] = 2
                
                if a-1 > -1 and b < len(mat[0]) and mat[a-1][b] == 1:
                    q.append([a-1, b])
                    mat[a-1][b] = 2
            
            if not len(q):
                break
            self.jvrc += 1
                
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    return -1
        
        return self.jvrc



        