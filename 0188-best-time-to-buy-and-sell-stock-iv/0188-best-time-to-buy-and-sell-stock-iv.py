class Solution:
    def maxProfit(self, k: int, arr: List[int]) -> int:
        dp = []
        for i in range(len(arr)):
            temp = []
            for j in range(k + 1):
                temp.append([-1] * 2)
            dp.append(temp)

        def func(i, arr, k, isBuy):
            if i >= len(arr) or k <= 0:
                return 0
            
            if dp[i][k][isBuy] != -1:
                return dp[i][k][isBuy]

            take, not_take = 0, 0

            if isBuy:
                take = func(i + 1, arr, k, 0) - arr[i]
                not_take = func(i + 1, arr, k, 1)
            else:
                take = func(i + 1, arr, k - 1, 1) + arr[i]
                not_take = func(i + 1, arr, k, 0)
            
            dp[i][k][isBuy] = max(take, not_take)
            return dp[i][k][isBuy]

        return func(0, arr, k, 1)
        