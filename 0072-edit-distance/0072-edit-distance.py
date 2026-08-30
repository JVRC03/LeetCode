class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        dp = []
        for i in range(len(s1) + 1):
            dp.append([-1] * (len(s2) + 1))
        
        for i in range(len(dp)):
            dp[i][0] = i
        
        for i in range(len(dp[0])):
            dp[0][i] = i

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]
        