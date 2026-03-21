class Solution:
    def reverseSubmatrix(self, mat: List[List[int]], x: int, y: int, k: int):
        f, r = x, x+k-1

        while f < r:
            for i in range(y, y+k):
                mat[f][i], mat[r][i] = mat[r][i], mat[f][i]
            
            f += 1
            r -= 1
                
        return mat
        