class Solution:
    def cherryPickup(self, mat: List[List[int]]) -> int:
        dp = []

        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[0])):
                curr = []
                for k in range(len(mat[0])):
                    curr.append(-1)
                temp.append(curr)
            dp.append(temp)
        
        def func(i, j1, j2, mat):
            if j1 < 0 or j1 >= len(mat[0]) or j2 < 0 or j2 >= len(mat[0]):
                return 0
            
            if i == len(mat)-1:
                if j1 == j2:
                    return mat[i][j2]
                return mat[i][j1] + mat[i][j2]
        
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]
            
            maxi = 0
            for x in range(-1, 2, 1):
                for y in range(-1, 2, 1):
                    val = 0

                    if j1 == j2:
                        val = mat[i][j1]
                    else:
                        val = mat[i][j1] + mat[i][j2]
                    
                    val += func(i+1, j1 + x, j2 + y, mat)
                
                    maxi = max(maxi, val)

            dp[i][j1][j2] = maxi
            return maxi
            
        return func(0, 0, len(mat[0])-1, mat)
        