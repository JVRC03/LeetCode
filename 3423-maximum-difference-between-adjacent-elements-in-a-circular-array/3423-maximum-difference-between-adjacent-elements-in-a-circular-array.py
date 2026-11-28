class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        jvrc = float('-inf')

        for i in range(len(nums) - 1):
            jvrc = max(jvrc, abs(nums[i] - nums[i + 1]))
        
        return max(jvrc, abs(nums[0] - nums[-1]))
        