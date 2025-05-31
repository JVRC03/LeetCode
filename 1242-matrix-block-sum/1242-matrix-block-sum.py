class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(mat)):
            for j in range(1, len(mat[0])):
                mat[i][j] += mat[i][j-1]
        
        jvrc = []

        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[0])):
                i_p, i_m = i+k, i-k
                j_p, j_m = j+k, j-k
                curr = 0

                if i_p >= len(mat):
                    i_p = len(mat)-1
                
                if i_m < 0:
                    i_m = 0
                
                if j_p >= len(mat[0]):
                    j_p = len(mat[0])-1
                
                if j_m <= 0:
                    j_m = -1
                
                i_diff = i_p-i_m+1

                for l in range(i_diff):
                    if j_m == -1:
                        curr += mat[i_p-l][j_p]
                    else:
                        curr += (mat[i_p-l][j_p]-mat[i_p-l][j_m-1])
                temp.append(curr)
            
            jvrc.append(temp)
        
        return jvrc

                    
                    






                
        