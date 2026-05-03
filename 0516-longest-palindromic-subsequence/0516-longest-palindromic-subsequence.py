class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        k = s[::-1]
        dp = []

        for i in range(len(s) + 1):
            temp = [0] * (len(s) + 1)
            dp.append(temp)
        jvrc = 0

        for i in range(1, len(s)+1):
            for j in range(1, len(s)+1):
                if s[i-1] == k[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                jvrc = max(jvrc, dp[i][j])
        
        return jvrc
        