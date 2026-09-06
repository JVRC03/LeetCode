class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = []
        for i in range(len(s)):
            dp.append([-1] * len(t))

        def func(i, j, s, t):
            if i < 0 and j < 0:
                return 1
            
            if i < 0:
                return 0

            if j < 0:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            val = 0
            if s[i] == t[j]:
                val = func(i - 1, j, s, t) + func(i - 1, j - 1, s, t)
            else:
                val = func(i - 1, j, s, t)
            
            dp[i][j] = val
            return dp[i][j]

        return func(len(s) - 1, len(t) - 1, s, t)
        