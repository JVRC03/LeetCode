class Solution:
    def uniquePaths(self, mat: List[List[int]]) -> int:
        dp = []

        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[0])):
                temp.append([-1] * 2)
            dp.append(temp)
        
        def func(i, j, mat, prev):
            if i >= len(mat) or j >= len(mat[0]):
                return 0

            if i == len(mat) - 1 and j == len(mat[0]) - 1:
                return 1
  
            if dp[i][j][prev] != -1:
                return dp[i][j][prev]

            right, down = 0, 0

            if mat[i][j] == 0:
                right = func(i, j + 1, mat, 1)
                down = func(i + 1, j, mat, 0)
            else:
                if prev == 0:
                    right = func(i, j + 1 , mat, 1)
                else:
                    down = func(i + 1, j, mat, 0)
                
            dp[i][j][prev] = right + down
            return right + down

        return func(0, 0, mat, -1) % 1000000007
        