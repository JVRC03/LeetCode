class Solution:
    def countCoveredBuildings(self, n: int, b: List[List[int]]) -> int:
        jvrc = 0
        col, row = {}, {}

        for i in range(len(b)):
            c = b[i][0]-1
            d = b[i][1]-1
            if c not in col:
                col[c] = [float('inf'), d]
            else:
                if d > col[c][1]:
                    col[c][0] = min(col[c][1], col[c][0])
                    col[c][1] = d
                else:
                    col[c][0] = min(col[c][0], d)
            
            if d not in row:
                row[d] = [float('inf'), c]
            else:
                if c > row[d][1]:
                    row[d][0] = min(row[d][1], row[d][0])
                    row[d][1] = c
                else:
                    row[d][0] = min(row[d][0], c)
            
        
        for t in range(len(b)):
            i = b[t][0]-1
            j = b[t][1]-1
            c = 0
            
            if i in col:
                if col[i][0] < j < col[i][1]:
                    c += 2
            if j in row:
                if row[j][0] < i < row[j][1]:
                    c += 2
            if c == 4:
                jvrc += 1
        
        return jvrc
        