class Solution:
    def shortestPathBinaryMatrix(self, mat: List[List[int]]) -> int:

        if mat[-1][-1] == 1 or mat[0][0] == 1:
            return -1

        q = deque([[0, 0, 0]])
        
        self.jvrc = 0

        while len(q):
            c = len(q)

            for idx in range(c):

                pair = q.popleft()

                curr = pair[0]
                i, j = pair[1], pair[2]

                if i == len(mat)-1 and j == len(mat[0])-1:
                    return self.jvrc + 1


                if i < len(mat) and j+1 < len(mat[0]) and mat[i][j+1] == 0:
                    mat[i][j+1] = 1
                    q.append([curr + 1, i, j+1])
                
                if i < len(mat) and j-1 > -1 and mat[i][j-1] == 0:
                    mat[i][j-1] = 1
                    q.append([curr + 1, i, j-1])
                
                if i+1 < len(mat) and j < len(mat[0]) and mat[i+1][j] == 0:
                    mat[i+1][j] = 1
                    q.append([curr + 1, i+1, j])
                
                if i-1 > -1 and j < len(mat[0]) and mat[i-1][j] == 0:
                    mat[i-1][j] = 1
                    q.append([curr + 1, i-1, j])


                if i-1 > -1 and j-1 > -1 and mat[i-1][j-1] == 0:
                    mat[i-1][j-1] = 1
                    q.append([curr + 1, i-1, j-1])
                
                if i-1 > -1 and j+1 < len(mat[0]) and mat[i-1][j+1] == 0:
                    q.append([curr + 1, i-1, j+1])
                    mat[i-1][j+1] = 1
                
                if i+1 < len(mat) and j-1 > -1 and mat[i+1][j-1] == 0:
                    mat[i+1][j-1] = 1
                    q.append([curr + 1, i+1, j-1])
                
                if i+1 < len(mat) and j+1 < len(mat[0]) and mat[i+1][j+1] == 0:
                    mat[i+1][j+1] = 1
                    q.append([curr + 1, i+1, j+1])
                
            self.jvrc += 1
        
        return -1





        