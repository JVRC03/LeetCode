class Solution:
    def maxUncrossedLines(self, s1: List[int], s2: List[int]) -> int:
        dp = []
        for i in range(len(s1)):
            temp = [-1] * len(s2)
            dp.append(temp)
        
        def func(s1, s2, i, j):
            
            if i < 0 or j < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            ans = -1
            if s1[i] == s2[j]:
                ans = 1 + func(s1, s2, i - 1, j - 1)
            else:
                ans = max(func(s1, s2, i - 1, j), func(s1, s2, i, j - 1))
            
            dp[i][j] = ans
            return dp[i][j]
        
        return func(s1, s2, len(s1) - 1, len(s2) - 1)
        