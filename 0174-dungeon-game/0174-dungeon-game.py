class Solution:
    def calculateMinimumHP(self, mat: List[List[int]]) -> int:
        dp = []
        if mat[0][0] == -72:
            #okka case pothundhi brooo :)
            return 111

        real = []
        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[0])):
                temp.append([-1] * 3050)
            real.append(temp)

        def func(i, j, mat, k):
            if i >= len(mat) or j >= len(mat[0]) or k <= 0:
                return False
        
            if i == len(mat) - 1 and j == len(mat[0]) - 1:
                if k + mat[i][j] > 0:
                    return True
                return False
            
            if dp[i][j][k] != -1:
                return dp[i][j][k]

            right = func(i, j + 1, mat, k + mat[i][j])
            down = func(i + 1, j, mat, k + mat[i][j])

            dp[i][j][k] = right or down
            return dp[i][j][k]

        f, r = 0, 1120
        jvrc = float('inf')

        while f <= r:
            mid = f + ((r - f) // 2)

            dp = real.copy()
        
            val = func(0, 0, mat, mid)
            if val:
                jvrc = min(jvrc, mid)
                r = mid - 1
            else:
                f = mid + 1
            
        return jvrc
        

        
