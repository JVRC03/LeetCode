class Solution:
    def minimumTotal(self, mat: List[List[int]]) -> int:

        for i in range(len(mat)-2, -1, -1):
            for j in range(len(mat[i])):
                mat[i][j] += min(mat[i+1][j], mat[i+1][j+1])

        return mat[0][0]
        
        