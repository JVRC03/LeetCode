class Solution:
    def minPathSum(self, mat: List[List[int]]) -> int:
        dp = []
        for i in range(len(mat)):
            dp.append([-1] * len(mat[0]))
        
        def func(i, j, mat):
            if i >= len(mat) or j >= len(mat[0]):
                return float('inf')

            if i == len(mat) - 1 and j == len(mat[0]) - 1:
                return mat[i][j]

            if dp[i][j] != -1:
                return dp[i][j]
            
            right = func(i, j + 1, mat)
            down = func(i + 1, j, mat)

            dp[i][j] = mat[i][j] + min(right, down)
            return dp[i][j]

        return func(0, 0, mat)
        