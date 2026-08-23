class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        temp = []
        for i in range(len(mat)):
            temp.append([0] * len(mat[0]))
        
        for i in range(len(mat)):
            temp[i][0] = mat[i][0]
        
        for i in range(len(mat[0])):
            temp[0][i] = mat[0][i]
        
        jvrc = 0
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][j] == 1:
                    temp[i][j] = 1 + min(temp[i - 1][j - 1], 
                    temp[i - 1][j], 
                    temp[i][j - 1])
        
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                jvrc += temp[i][j]
        
        return jvrc


        