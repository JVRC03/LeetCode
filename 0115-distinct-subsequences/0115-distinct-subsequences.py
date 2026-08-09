class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = []

        for i in range(len(s) + 1):
            temp = [0] * (len(t) + 1)
            dp.append(temp)
        
        for i in range(len(dp)):
            dp[i][0] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
        