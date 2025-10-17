class Solution:
    def matrixScore(self, mat: List[List[int]]) -> int:
        jvrc = 0

        for i in range(len(mat)):
            if mat[i][0] == 1:
                continue
            
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = 0
                else:
                    mat[i][j] = 1
        
        for i in range(len(mat[0])-1, -1, -1):
            c = 0
            for j in range(len(mat)):
                if mat[j][i] == 1:
                    c += 1
            
            if c > len(mat)//2:
                continue
            for j in range(len(mat)):
                if c:
                    mat[j][i] = 0
                    c-=1
                else:
                    mat[j][i] = 1
            
        for i in range(len(mat)):
            s = ''
            for j in range(len(mat[i])):
                s += str(mat[i][j])
            
            jvrc += int(s, 2)
    
        return jvrc

        