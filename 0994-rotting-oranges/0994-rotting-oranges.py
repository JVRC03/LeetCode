class Solution:
    def orangesRotting(self, mat: List[List[int]]) -> int:
        q = deque([])
        not_rot, jvrc = 0, 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 2:
                    q.append([i, j])
                elif mat[i][j] == 1:
                    not_rot += 1
        
        if not_rot == 0:
            return 0
        if not len(q):
            return -1
        
        while len(q):
            c = len(q)

            for idx in range(c):
                pair = q.popleft()

                i, j = pair[0], pair[1]

                if j+1 < len(mat[0]) and mat[i][j+1] == 1:
                    q.append([i, j+1])
                    mat[i][j+1] = 0
                
                if j-1 > -1 and mat[i][j-1] == 1:
                    q.append([i, j-1])
                    mat[i][j-1] = 0

                if i+1 < len(mat) and mat[i+1][j] == 1:
                    q.append([i+1, j])
                    mat[i+1][j] = 0

                if i-1 > -1 and mat[i-1][j] == 1:
                    q.append([i-1, j])
                    mat[i-1][j] = 0
            if len(q):
                jvrc += 1      

        for i in range(len(mat)):
            if 1 in mat[i]:
                return -1  
        
        return jvrc