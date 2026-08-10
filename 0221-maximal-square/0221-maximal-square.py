class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        dp = []
        for i in range(len(mat)):
            temp = [0] * len(mat[0])
            for j in range(len(mat[i])):
                mat[i][j] = int(mat[i][j])
            dp.append(temp)
    
        jvrc = 0
        for i in range(len(mat)):
            dp[i][0] = mat[i][0]
            jvrc = max(jvrc, dp[i][0] ** 2)

        for i in range(len(mat[0])):
            dp[0][i] = mat[0][i]
            jvrc = max(jvrc, dp[0][i] ** 2)

        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][j]:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

                jvrc = max(jvrc, dp[i][j] ** 2)
        
        return jvrc

        