class Solution:
    def differenceOfDistinctValues(self, mat: List[List[int]]) -> List[List[int]]:
        jvrc = []

        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[0])):
                temp.append(0)
            jvrc.append(temp)

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                l, r = set(), set()
                c = 1

                for k in range(i-1, -1, -1):
                    if j-c < 0:
                        break
                    l.add(mat[k][j-c])
                    c += 1
                c = 1

                for k in range(i+1, len(mat)):
                    if j+c >= len(mat[0]):
                        break
                    r.add(mat[k][j+c])
                    c += 1

                jvrc[i][j] = abs(len(l) - len(r))
        
        return jvrc
        