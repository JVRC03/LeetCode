class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = []
        for i in range(n + 1):
            dp.append([-1] * (n + 1))
        
        def func(i, x, k):
            if k == 0:
                return 1
            
            if k < 0 or (i ** x) > k:
                return 0

            if dp[i][k] != -1:
                return dp[i][k]

            take = 0
            if k - (i ** x) >= 0:
                take = func(i + 1, x, k - (i ** x))
            
            not_take = func(i + 1, x, k)

            dp[i][k] = take + not_take
            return dp[i][k]

        return func(1, x, n) % 1000000007
        