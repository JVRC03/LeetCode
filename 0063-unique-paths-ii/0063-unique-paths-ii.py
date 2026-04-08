class Solution:
    def uniquePathsWithObstacles(self, mat: List[List[int]]) -> int:
        dp = []
        for i in range(len(mat)):
            temp = [-1] * len(mat[0])
            dp.append(temp)

        def f(mat, i, j):
            if i >= len(mat) or j >= len(mat[0]) or i < 0 or j < 0 or mat[i][j] == 1:
                return 0
            
            if i == len(mat)-1 and j == len(mat[0]) - 1:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]

            right = f(mat, i, j+1)
            down = f(mat, i+1, j)

            dp[i][j] = right + down

            return dp[i][j]
            
        return f(mat, 0, 0)

        