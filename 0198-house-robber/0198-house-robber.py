class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def dfs(arr, idx):
            if idx >= len(arr):
                return 0
            
            if dp[idx] != -1:
                return dp[idx]
            
            take = arr[idx] + dfs(arr, idx + 2)
            not_take = dfs(arr, idx + 1)

            dp[idx] = max(take, not_take)

            return dp[idx]

        return dfs(nums, 0)
        