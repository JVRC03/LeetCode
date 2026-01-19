class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        f, r = 0, 2
        jvrc = 0

        while f < r and r < len(nums):
            if nums[f] + nums[r] == nums[r-1]/2:
                jvrc += 1
            f += 1
            r += 1
        
        return jvrc
        