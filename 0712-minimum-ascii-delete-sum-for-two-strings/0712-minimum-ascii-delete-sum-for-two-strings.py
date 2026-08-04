class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        dp = []
        for i in range(len(s1) + 1):
            temp = [-1] * (len(s2) + 1)
            dp.append(temp)

        def func(s1, s2, i, j):
            
            if i < 0 and j < 0:
                return 0
            
            if i < 0:
                count = 0
                for idx in range(j + 1):
                    count += ord(s2[idx])
                return count
            
            if j < 0:
                count = 0
                for idx in range(i + 1):
                    count += ord(s1[idx])
                return count
            
            if dp[i][j] != -1:
                return dp[i][j]

            ans = -1
            if s1[i] == s2[j]:
                ans = func(s1, s2, i-1, j-1)
            else:
                ans = min(ord(s1[i]) + func(s1, s2, i-1, j), ord(s2[j])+func(s1, s2, i, j-1))
            
            dp[i][j] = ans

            return dp[i][j]

        return func(s1, s2, len(s1) - 1, len(s2) - 1)
        