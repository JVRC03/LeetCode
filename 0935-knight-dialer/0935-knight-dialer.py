class Solution:
    def knightDialer(self, n: int) -> int:
        mat = [
            [1, 2, 3], 
            [4, 5, 6],
            [7, 8, 9], 
            ['X', 0, 'X']
        ]
        dp = []
        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[0])):
                temp.append([-1] * (n + 1))
            dp.append(temp)

        def func(i, j, n):
            if mat[i][j] == 'X':
                return 0

            if n == 0:
                return 1
            
            if dp[i][j][n] != -1:
                return dp[i][j][n]

            a, b, c, d = 0, 0, 0, 0

            if i - 1 >= 0 and j - 2 >= 0:
                a = func(i - 1, j - 2, n - 1)
            if i - 2 >= 0 and j - 1 >= 0:
                b = func(i - 2, j - 1, n - 1)
            if i - 2 >= 0 and j + 1 < len(mat[0]):
                c = func(i - 2, j + 1, n - 1)
            if i - 1 >= 0 and j + 2 < len(mat[0]):
                d = func(i - 1, j + 2, n - 1)

            e, f, g, h = 0, 0, 0, 0

            if i + 1 < len(mat) and j - 2 >= 0:
                e = func(i + 1, j - 2, n - 1)
            if i + 2 < len(mat) and j - 1 >= 0:
                f = func(i + 2, j - 1, n - 1)
            if i + 2 < len(mat) and j + 1 < len(mat[0]):
                g = func(i + 2, j + 1, n - 1)
            if i + 1 < len(mat) and j + 2 < len(mat[0]):
                h = func(i + 1, j + 2, n - 1)

            dp[i][j][n] = ((a + b + c + d) + (e + f + g + h)) % 1000000007
            return dp[i][j][n]

        jvrc = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 'X':
                    jvrc += func(i, j, n - 1)
        
        return jvrc % 1000000007
        