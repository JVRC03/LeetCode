class Solution:
    def maxMatrixSum(self, mat: List[List[int]]) -> int:
        jvrc = 0
        curr = float('inf')
        c = 0

        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j] < 0:
                    c += 1
                curr = min(curr, abs(mat[i][j]))
                jvrc += abs(mat[i][j])
                
        if not c%2:
            return jvrc

        curr *= -2
        return jvrc+curr


        