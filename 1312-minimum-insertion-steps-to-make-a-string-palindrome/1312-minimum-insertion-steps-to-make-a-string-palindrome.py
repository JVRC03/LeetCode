class Solution:
    def minInsertions(self, s: str) -> int:
        dp = []
        for i in range(len(s)):
            dp.append([-1] * len(s))

        def func(i, j, s1, s2):
            if i < 0 or j < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            val = 0
            if s1[i] == s2[j]:
                val = 1 + func(i - 1, j - 1, s1, s2)
            else:
                val = max(func(i - 1, j, s1, s2), func(i, j - 1, s1, s2))
            
            dp[i][j] = val
            return dp[i][j]

        return len(s) - func(len(s) - 1, len(s) - 1, s, s[::-1])
        