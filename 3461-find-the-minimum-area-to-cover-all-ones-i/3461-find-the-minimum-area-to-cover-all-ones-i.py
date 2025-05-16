class Solution:
    def minimumArea(self, mat: List[List[int]]) -> int:
        up, down, left, right = -1, -1, float('inf'), float('-inf')

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    if up == -1:
                        up = i
                    down = i
                    if j < left:
                        left = j
                    if j > right:
                        right = j
        
        jv = down-up+1
        rc = right-left+1

        return jv*rc
        