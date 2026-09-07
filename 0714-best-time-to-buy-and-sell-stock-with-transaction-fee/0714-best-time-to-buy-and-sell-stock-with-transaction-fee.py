class Solution:
    def maxProfit(self, arr: List[int], k: int) -> int:
        dp = []
        for i in range(2):
            dp.append([-1] * len(arr))

        def func(i, arr, canBuy, k):
            if i == len(arr):
                return 0
            
            if dp[canBuy][i] != -1:
                return dp[canBuy][i]

            take, not_take = 0, 0
            if canBuy:
                take = func(i + 1, arr, 0, k) - k - arr[i]
                not_take = func(i + 1, arr, 1, k)
            else:
                take = func(i + 1, arr, 1, k) + arr[i]
                not_take = func(i + 1, arr, 0, k)
            
            dp[canBuy][i] = max(take, not_take)
            return dp[canBuy][i]

        return func(0, arr, 1, k)
        