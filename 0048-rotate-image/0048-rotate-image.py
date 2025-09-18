class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        for i in range(len(mat)):
            for k in range(i+1, len(mat)):
                mat[i][k], mat[k][i] = mat[k][i], mat[i][k]
        
        for i in range(len(mat)):
            mat[i] = mat[i][::-1]
        
        return mat
            

        