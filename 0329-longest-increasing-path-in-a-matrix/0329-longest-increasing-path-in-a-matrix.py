class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        dp = []
        for i in range(len(mat)):
            dp.append([-1] * len(mat[0]))
        
        def func(i, j, mat, prev):
            if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]) or mat[i][j] <= prev:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            u = func(i - 1, j, mat, mat[i][j])
            d = func(i + 1, j, mat, mat[i][j])
            l = func(i, j - 1, mat, mat[i][j])
            r = func(i, j + 1, mat, mat[i][j])

            dp[i][j] = 1 + max(l, r, u, d)
            return dp[i][j]

        jvrc = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if dp[i][j] == -1:
                    func(i, j, mat, -1)
                
                jvrc = max(jvrc, dp[i][j])
        
        return jvrc
        