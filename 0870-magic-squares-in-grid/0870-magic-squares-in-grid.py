class Solution:
    def numMagicSquaresInside(self, mat: List[List[int]]) -> int:
        if len(mat) < 3 or len(mat[0]) < 3:
            return 0
        
        jvrc = 0

        for i in range(len(mat)-2):
            for j in range(len(mat[0])-2):
                s = set()
                r1 = mat[i][j]+mat[i][j+1]+mat[i][j+2]
                r2 = mat[i+1][j]+mat[i+1][j+1]+mat[i+1][j+2]
                r3 = mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2]

                c1 = mat[i][j]+mat[i+1][j]+mat[i+2][j]
                c2 = mat[i][j+1]+mat[i+1][j+1]+mat[i+2][j+1]
                c3 = mat[i][j+2]+mat[i+1][j+2]+mat[i+2][j+2]

                d1 = mat[i][j]+mat[i+1][j+1]+mat[i+2][j+2]
                d2 = mat[i][j+2]+mat[i+1][j+1]+mat[i+2][j]

                s.add(mat[i][j])
                s.add(mat[i][j+1])
                s.add(mat[i][j+2])

                s.add(mat[i+1][j])
                s.add(mat[i+1][j+1])
                s.add(mat[i+1][j+2])

                s.add(mat[i+2][j])
                s.add(mat[i+2][j+1])
                s.add(mat[i+2][j+2])

                if r1 == r2 == r3 == c1 == c3 == c3 == d1 == d2:
                    d = 0
                    for k in range(10, 16):
                        if k in s:
                            d = 1
                            break
                    if d or 0 in s:
                        continue
                    if len(s) == 9:
                        jvrc += 1
        
        return jvrc


        