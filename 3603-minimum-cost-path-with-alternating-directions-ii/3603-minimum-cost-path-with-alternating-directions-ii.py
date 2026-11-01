class Solution:
    def minCost(self, m: int, n: int, mat: List[List[int]]) -> int:
        dp = []

        for i in range(m):
            temp = []
            for j in range(n):
                temp.append([-1] * 2)
            dp.append(temp)

        def func(i, j, mat, sec):

            if i >= len(mat) or j >= len(mat[0]):
                return float('inf')

            if i == len(mat) - 1 and j == len(mat[0]) - 1:
                return ((i + 1) * (j + 1))
            
            if dp[i][j][sec] != -1:
                return dp[i][j][sec]

            ans = mat[i][j] + ((i + 1) * (j + 1))

            right = func(i, j + 1, mat, (sec + 1) % 2)
            down = func(i + 1, j, mat, (sec + 1) % 2)

            dp[i][j][sec] = ans + min(right, down)

            return dp[i][j][sec]

        return 1 + min(func(0, 1, mat, 1), func(1, 0, mat, 1))
        