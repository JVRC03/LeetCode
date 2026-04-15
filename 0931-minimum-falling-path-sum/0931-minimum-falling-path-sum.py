class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:

        for i in range(len(mat)-2, -1, -1):
            for j in range(len(mat[i])):
                a, b, c = float('inf'), mat[i+1][j], float('inf')

                if j-1 >= 0:
                    a = mat[i+1][j-1]
                if j+1 < len(mat[i]):
                    c = mat[i+1][j+1]
                
                mat[i][j] += min(a, b, c) 
        
        return min(mat[0])