class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peak, val = 0, 0

        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                peak += nums[i]
            
            if nums[i - 1] > nums[i] < nums[i + 1]:
                val += nums[i]
        
        return peak - val
        