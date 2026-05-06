class Solution:
    def rotateTheBox(self, mat: List[List[str]]) -> List[List[str]]:
        jvrc = []
        for i in range(len(mat)):
            temp = ['.'] * len(mat[0])
            jvrc.append(temp)
        
        for i in range(len(mat)):
            c = 0
            for j in range(len(mat[0])):
                if mat[i][j] == '#':
                    c += 1
                elif mat[i][j] == '*':
                    jvrc[i][j] = '*'
                    idx = 1
                    while c:
                        c -= 1
                        jvrc[i][j-idx] = '#'
                        idx += 1
            
            if c:
                idx = len(mat[0])-1
                while c:
                    c -= 1
                    jvrc[i][idx] = '#'
                    idx -= 1
        mat = []
        for i in range(len(jvrc[0])):
            temp = []
            for j in range(len(jvrc)-1, -1, -1):
                temp.append(jvrc[j][i])
            mat.append(temp)
        
        return mat

        