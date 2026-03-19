class Solution:
    def numberOfSubmatrices(self, mat: List[List[str]]) -> int:
        top = []
        jvrc = 0
        temp = []

        for i in range(len(mat[0])):
            x, y = 0, 0
            if mat[0][i] == 'X':
                x += 1
            elif mat[0][i] == 'Y':
                y += 1
            
            if not len(temp):
                temp.append([x, y])
            else:
                temp.append([x+temp[-1][0], y+temp[-1][-1]])
            
            if temp[-1][-1] == temp[-1][-2] and temp[-1][-1] > 0:
                jvrc += 1
        
        top.append(temp)
        
        for i in range(1, len(mat)):
            local_x, local_y = 0, 0
            temp = []

            for j in range(len(mat[0])):
                if mat[i][j] == 'X':
                    local_x += 1
                elif mat[i][j] == 'Y':
                    local_y += 1
                
                tot_x, tot_y = local_x+top[i-1][j][0], local_y+top[i-1][j][1]

                if tot_x == tot_y and tot_x > 0:
                    jvrc += 1
                
                temp.append([tot_x, tot_y])
            
            top.append(temp)

        return jvrc
                




        