class Solution:
    def cherryPickup(self, mat: List[List[int]]) -> int:
        dp = []
        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[0])):
                temp.append([-1] * len(mat[0]))
            dp.append(temp)

        def func(i, j1, j2, mat):

            if i >= len(mat) or j1 >= len(mat[0]) or j2 >= len(mat[0]) or j1 < 0 or j2 < 0:
                return 0
           
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]

            a = func(i + 1, j1 - 1, j2 - 1, mat)
            b = func(i + 1, j1 - 1, j2, mat)
            c = func(i + 1, j1 - 1, j2 + 1, mat)

            d = func(i + 1, j1, j2 - 1, mat)
            e = func(i + 1, j1, j2, mat)
            f = func(i + 1, j1, j2 + 1, mat)

            g = func(i + 1, j1 + 1, j2 - 1, mat)
            h = func(i + 1, j1 + 1, j2, mat)
            jvrc=func(i + 1, j1 + 1, j2 + 1, mat)

            val = 0
            if j1 == j2:
                val = mat[i][j1]
            else:
                val = mat[i][j1] + mat[i][j2]

            dp[i][j1][j2] = val + max(a, b, c, d, e, f, g, h, jvrc)
            return dp[i][j1][j2]

        ans = func(0, 0, len(mat[0])-1, mat)
        return ans
        