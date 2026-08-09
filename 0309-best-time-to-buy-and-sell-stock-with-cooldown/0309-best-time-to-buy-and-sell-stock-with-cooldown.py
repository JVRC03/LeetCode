class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        dp = []
        for i in range(2):
            temp = [-1] * len(arr)
            dp.append(temp)

        def func(idx, arr, buy):
            if idx >= len(arr):
                return 0
            
            if dp[buy][idx] != -1:
                return dp[buy][idx]

            take, not_take = -1, -1
            if buy:
                take = func(idx + 1, arr, 0) - arr[idx]
                not_take = func(idx + 1, arr, 1)
            else:
                take = arr[idx] + func(idx + 2, arr, 1)
                not_take = func(idx + 1, arr, 0)
            
            dp[buy][idx] = max(take, not_take)
            return dp[buy][idx]

        return func(0, arr, 1)
        