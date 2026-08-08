class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def func(idx, arr):
            if idx >= len(arr)-1:
                return 0
            
            if dp[idx] != -1:
                return dp[idx]

            glob = float('inf')
            for i in range(1, arr[idx] + 1):
                glob = min(glob, 1 + func(idx + i, arr))

            dp[idx] = glob
            return dp[idx]

        if len(nums) < 3:
            return len(nums) - 1
        return func(0, nums)




        