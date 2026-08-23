class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp = []
        for i in range(len(nums)):
            dp.append([-1] * (k + 1))

        def func(idx, nums, k):
            if idx == len(nums):
                if k == 0:
                    return 0
                return float('-inf')

            if k <= 0:
                return float('-inf')

            if dp[idx][k] != -1:
                return dp[idx][k]

            maxi = 0
            arr = []

            for i in range(idx, len(nums)):
                arr.append(nums[i])
                curr = (sum(arr) / len(arr)) + func(i + 1, nums, k - 1)
                
                maxi = max(maxi, curr)
            
            dp[idx][k] = maxi
            return dp[idx][k]

        return func(0, nums, k)
        