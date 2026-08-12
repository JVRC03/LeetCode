class Solution:
    def combinationSum4(self, nums: List[int], k: int) -> int:
        dp = [-1] * (k+1)

        def func(arr, k, curr):
            if curr > k:
                return 0
            
            if dp[curr] != -1:
                return dp[curr]

            if curr == k:
                return 1

            tot = 0
            for i in range(len(arr)):
                tot += func(arr, k, curr + arr[i]) 
            
            dp[curr] = tot
            return dp[curr]

        return func(nums, k, 0)
        