class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = []
        for i in range(len(s)):
            dp.append([-1] * len(p))

        def func(i, j, s, t):
            if i < 0 and j < 0:
                return True
            
            if j < 0:
                return False
            
            if i < 0:
                for idx in range(j + 1):
                    if t[idx] != '*':
                        return False
                return True

            if dp[i][j] != -1:
                return dp[i][j]
            
            val = 0
            if s[i] == t[j] or t[j] == '?':
                val = func(i - 1, j - 1, s, t)
            elif t[j] == '*':
                val = func(i, j - 1, s, t) or func(i - 1, j, s, t)
            else:
                val = False
            
            dp[i][j] = val
            return dp[i][j]

        return func(len(s) - 1, len(p) - 1, s, p)
        
        