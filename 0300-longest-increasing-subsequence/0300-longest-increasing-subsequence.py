class Solution:
    def f(self, nums, idx, dp, curr):
        if idx >= len(nums):
            return 0
        
        if dp[idx] != -1:
            return dp[idx]
        
        glob = 1

        for i in range(idx, len(nums)):
            if nums[i] > curr:
                k = 1+self.f(nums, i, dp, nums[i])
                glob = max(k, glob)
        
        dp[idx] = glob

        return dp[idx]

    def lengthOfLIS(self, nums: List[int]) -> int:
        jvrc = 0
        dp = [-1] * len(nums)

        for i in range(len(nums)):
            if dp[i] != -1:
                continue
            val = self.f(nums, i, dp, nums[i])

            jvrc = max(jvrc, val)
            
        self.f(nums, 0, dp, nums[0])


        return jvrc
        