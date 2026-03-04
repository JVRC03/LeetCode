class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row, col = {}, {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if i not in row:
                        row[i] = 1
                    else:
                        row[i] += 1
                    
                    if j not in col:
                        col[j] = 1
                    else:
                        col[j] += 1
        
        jvrc = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if (row[i]) == 1 and (col[j]) == 1:
                        jvrc += 1
                        continue
        
        return jvrc


        