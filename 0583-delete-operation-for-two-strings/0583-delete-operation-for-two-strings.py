class Solution:
    def minDistance(self, a: str, b: str) -> int:
        dp = []

        for i in range(len(a) + 1):
            temp = [0] * (len(b) + 1)
            dp.append(temp)

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if a[i-1] == b[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return (len(a) - dp[-1][-1]) + (len(b) - dp[-1][-1]) 