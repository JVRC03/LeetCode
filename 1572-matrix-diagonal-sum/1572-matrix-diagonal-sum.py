class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        col = len(mat[0])-1

        jvrc = 0
        st = 0

        for i in range(len(mat)):
            jvrc += mat[i][col]
            jvrc += mat[i][st]
            if i == col:
                jvrc -= mat[i][st]
            col -= 1
            st += 1
        
        return jvrc
        