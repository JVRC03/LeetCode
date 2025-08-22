class Solution:
    def minimumArea(self, mat: List[List[int]]) -> int:
        fi, fj = -1, -1
        ri, rj = float('inf'), -1

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if fi == -1:
                        fi = i
                    ri = min(ri, j)

                    fj = max(i, fj)
                    rj = max(j, rj) 

        jvrc = ((rj-ri)+1) * ((fj-fi)+1)

        return jvrc
        