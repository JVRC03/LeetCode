class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = []

        for i in range(n+1):
            dp.append([-1] * (target + 1))

        def func(n, k, tar):
            if n == 0 and tar == 0:
                return 1
            
            if n < 0 or tar < 0:
                return 0

            if dp[n][tar] != -1:
                return dp[n][tar]

            glob = 0
            for i in range(1, k + 1):
                take = 0
                if tar - i >= 0:
                    take = func(n - 1, k, tar - i)
                else:
                    break

                glob += take

            dp[n][tar] = glob
            return dp[n][tar]

        return func(n, k, target) % 1000000007
        