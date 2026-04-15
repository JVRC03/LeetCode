class Solution:
    def minPathSum(self, mat: List[List[int]]) -> int:
        dp = []

        for i in range(len(mat)):
            temp = [-1] * len(mat[0])
            dp.append(temp)
        
        def func(mat, i, j):
            if i >= len(mat) or j >= len(mat[0]):
                return float('inf')

            if i == len(mat)-1 and j == len(mat[0])-1:
                dp[i][j] = mat[i][j]
                return mat[i][j]

            if dp[i][j] != -1:
                return dp[i][j]

            right = func(mat, i, j+1)
            down = func(mat, i+1, j)

            dp[i][j] = mat[i][j] + min(right, down)

            return dp[i][j]
        
        return func(mat, 0, 0)




        