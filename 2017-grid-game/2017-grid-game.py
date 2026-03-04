class Solution:
    def gridGame(self, mat: List[List[int]]) -> int:
        p_sum, temp = [], []

        for i in range(len(mat[0])-1, -1, -1):
            if not len(temp):
                temp.append(mat[0][i])
            else:
                temp.append(temp[-1] + mat[0][i])
        temp = temp[::-1]
        p_sum.append(temp)

        temp = []

        for i in range(len(mat[0])):
            if not len(temp):
                temp.append(mat[1][0])
            else:
                temp.append(temp[-1] + mat[1][i])
        p_sum.append(temp)

        mat[0][0] = 0
        mat[-1][-1] = 0
        idx = -1
        jvrc = -1

        for i in range(1, len(mat[0])):
            if p_sum[0][i] > p_sum[1][i-1]:
                continue
            jvrc = p_sum[0][i] 
            idx = i-1
            break
        curr = 0

        if idx == -1:
            idx = len(mat[0])-1
        
        for i in range(idx):
            curr += mat[1][i]
        
        return max(jvrc, curr)
        



            


        

        