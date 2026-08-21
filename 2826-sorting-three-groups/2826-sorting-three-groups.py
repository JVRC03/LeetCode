class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dp = []

        for i in range(len(nums)):
            dp.append([-1] * len(nums))

        def func(i, arr, prev):
            if i == len(arr):
                return 0
            
            if dp[i][prev] != -1:
                return dp[i][prev]

            take = 0
            if prev == -1 or arr[prev] <= arr[i]:
                take = 1 + func(i + 1, arr, i)
            
            not_take = func(i + 1, arr, prev)

            dp[i][prev] = max(take, not_take)
            return dp[i][prev]

        return len(nums) - func(0, nums, -1)
        