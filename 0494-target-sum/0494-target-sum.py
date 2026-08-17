class Solution:
    def findTargetSumWays(self, nums: List[int], diff: int) -> int:
        dp, tot = [], sum(nums)
        k = (tot - diff) / 2

        if k != int(k):
            return 0
        k = int(k)

        for i in range(len(nums)):
            dp.append([-1] * (k + 1))

        def func(i, arr, k):
            if i == len(arr):
                if k == 0:
                    return 1
                
                return 0
            
            if k < 0:
                return 0
            
            if dp[i][k] != -1:
                return dp[i][k]

            take = func(i + 1, arr, k - arr[i])
            not_take = func(i + 1, arr, k)

            dp[i][k] = take + not_take
            return dp[i][k]
            
        return func(0, nums, k)
        