class Solution:
    def findPaths(self, row: int, col: int, k: int, i: int, j: int) -> int:
        i += 1
        j += 1
        dp = []

        for jim in range(row + 1):
            temp = []
            for kim in range(col + 1):
                temp.append([-1] * (k + 1))
            dp.append(temp)
        
        def func(i, j, row, col, k):
            if i <= 0 or i > row or j <= 0 or j > col:
                return 1
            
            if k <= 0:
                return 0

            if dp[i][j][k] != -1:
                return dp[i][j][k]

            left = func(i, j - 1, row, col, k - 1)
            right = func(i, j + 1, row, col, k - 1)
            top = func(i - 1, j, row, col, k - 1)
            down = func(i + 1, j, row, col, k - 1)

            dp[i][j][k] = left + right + top + down
            return dp[i][j][k]

        return func(i, j, row, col, k) % 1000000007
        