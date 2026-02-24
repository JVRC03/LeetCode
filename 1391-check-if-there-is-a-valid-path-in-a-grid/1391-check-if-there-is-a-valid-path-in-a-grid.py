class Solution:
    def hasValidPath(self, mat: List[List[int]]) -> bool:
        q = deque([[mat[0][0], 0, 0]])
        mat[0][0] = -1

        while len(q):
            c = len(q)

            for idx in range(c):
                pair = q.popleft()

                node = pair[0]
                i, j = pair[1], pair[2]
                
                if i == len(mat)-1 and j == len(mat[0])-1:
                    return True

                if node == 1:
                    if i < len(mat) and j+1 < len(mat[0]) and mat[i][j+1] in {1, 3, 5}:
                        q.append([mat[i][j+1], i, j+1])
                        mat[i][j+1] = -1
                    if i < len(mat) and j-1 > -1 and mat[i][j-1] in {1, 4, 6}:
                        q.append([mat[i][j-1], i, j-1])
                        mat[i][j-1] = -1
                
                if node == 2:
                    if i+1 < len(mat) and j < len(mat[0]) and mat[i+1][j] in {2, 5, 6}:
                        q.append([mat[i+1][j], i+1, j])
                        mat[i+1][j] = -1
                    if i-1 > -1 and j < len(mat[0]) and mat[i-1][j] in {2, 3, 4}:
                        q.append([mat[i-1][j], i-1, j])
                        mat[i-1][j] = -1
                
                if node == 3:
                    if i+1 < len(mat) and j < len(mat[0]) and mat[i+1][j] in {2, 5, 6}:
                        q.append([mat[i+1][j], i+1, j])
                        mat[i+1][j] = -1
                    if i < len(mat) and j-1 > -1 and mat[i][j-1] in {1, 4, 6}:
                        q.append([mat[i][j-1], i, j-1])
                        mat[i][j-1] = -1
                
                if node == 4:
                    if i+1 < len(mat) and j < len(mat[0]) and mat[i+1][j] in {2, 5, 6}:
                        q.append([mat[i+1][j], i+1, j])
                        mat[i+1][j] = -1
                    if i < len(mat) and j+1 < len(mat[0]) and mat[i][j+1] in {3, 5, 1}:
                        q.append([mat[i][j+1], i, j+1])
                
                if node == 5:
                    if i < len(mat) and j-1 > -1 and mat[i][j-1] in {4, 6, 1}:
                        q.append([mat[i][j-1], i, j-1])
                        mat[i][j-1] = -1
                    if i-1 > -1 and j < len(mat[0]) and mat[i-1][j] in {3, 4, 2}:
                        q.append([mat[i-1][j], i-1, j])
                        mat[i-1][j] = -1

                if node == 6:
                    if i < len(mat) and j+1 < len(mat[0]) and mat[i][j+1] in {3, 5, 1}:
                        q.append([mat[i][j+1], i, j+1])
                        mat[i][j+1] = -1
                    if i-1 > -1 and j < len(mat[0]) and mat[i-1][j] in {4, 3, 2}:
                        q.append([mat[i-1][j], i-1, j])
                        mat[i-1][j] = -1
            
        
        return False
                


                    
        